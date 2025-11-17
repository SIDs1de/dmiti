import { useState } from "react";
import type { PolynomialSubPPResponse, Rational } from "../../types/api";
import { algebraApi } from "../../services/api";
import { Button, Typography } from "antd";
import { PolynomialInput, type Monomial } from "../../shared/PolynomialInput";

export const SUB_PP_P = () => {
  const [polynomialA, setPolynomialA] = useState<Monomial[]>([
    {
      coefficient: {
        numerator: null,
        denominator: null,
      },
      degree: null,
    },
  ]);

  const [polynomialB, setPolynomialB] = useState<Monomial[]>([
    {
      coefficient: {
        numerator: null,
        denominator: null,
      },
      degree: null,
    },
  ]);

  const [result, setResult] = useState<PolynomialSubPPResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const uiToApiFormat = (uiPolynomial: typeof polynomialA) => {
    const coefficients: { [degree: string]: Rational } = {};

    for (const monomial of uiPolynomial) {
      if (
        monomial.coefficient.numerator !== null &&
        monomial.coefficient.denominator !== null &&
        monomial.degree !== null
      ) {
        const numerator = Number(monomial.coefficient.numerator);
        const denominator = Number(monomial.coefficient.denominator);
        const degree = monomial.degree;

        if (isNaN(numerator) || isNaN(denominator) || denominator === 0) {
          throw new Error("Некорректные значения коэффициентов");
        }

        if (degree in coefficients) {
          throw new Error(`Степень ${degree} повторяется в полиноме`);
        }

        coefficients[degree] = {
          numerator: {
            sign: numerator >= 0 ? 0 : 1,
            absolute: Math.abs(numerator),
          },
          denominator: {
            digits: String(denominator)
              .split("")
              .map((d) => Number(d)),
          },
        };
      }
    }

    if (Object.keys(coefficients).length === 0) {
      throw new Error("Полином не может быть пустым");
    }

    return { coefficients };
  };

  const handleClick = async () => {
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const polyA = uiToApiFormat(polynomialA);
      const polyB = uiToApiFormat(polynomialB);

      const response = await algebraApi.polynomialSubPP({
        a: polyA,
        b: polyB,
      });

      setResult(response);
    } catch (error) {
      console.error("Failed:", error);
      setError((error as Error).message);
      setResult({
        success: false,
        result: {
          coefficients: {},
          degree: 0,
          string: "",
        },
        error: (error as Error).message,
      });
    }

    setLoading(false);
  };

  const hasEmptyFields = () => {
    const checkPolynomial = (poly: typeof polynomialA) => {
      return poly.some(
        (monomial) =>
          monomial.coefficient.numerator === null ||
          monomial.coefficient.denominator === null ||
          monomial.degree === null,
      );
    };

    return checkPolynomial(polynomialA) || checkPolynomial(polynomialB);
  };

  return (
    <section>
      <Typography.Title level={2}>SUB_PP_P: Вычитание многочленов</Typography.Title>

      <div style={{ marginBottom: "24px" }}>
        <Typography.Text strong>Первый полином:</Typography.Text>
        <PolynomialInput
          value={polynomialA}
          onChange={setPolynomialA}
        />
      </div>

      <div style={{ marginBottom: "24px" }}>
        <Typography.Text strong>Второй полином:</Typography.Text>
        <PolynomialInput
          value={polynomialB}
          onChange={setPolynomialB}
        />
      </div>

      <Button
        onClick={handleClick}
        disabled={loading || hasEmptyFields()}
        style={{ marginBottom: "16px" }}
      >
        Вычислить разность
      </Button>

      {error && <Typography.Paragraph>Ошибка: {error}</Typography.Paragraph>}

      {result && (
        <div>
          <Typography.Title level={3}>Результат вычитания:</Typography.Title>
          {result.success ? (
            <div>
              <Typography.Paragraph>
                <strong>Строковое представление:</strong> {result.result.string}
              </Typography.Paragraph>
              <Typography.Paragraph>
                <strong>Степень полинома:</strong> {result.result.degree}
              </Typography.Paragraph>
              <Typography.Paragraph>
                <strong>Коэффициенты:</strong>
              </Typography.Paragraph>
              <pre
                style={{
                  background: "#f5f5f5",
                  padding: "12px",
                  borderRadius: "6px",
                  overflow: "auto",
                }}
              >
                {JSON.stringify(result.result.coefficients, null, 2)}
              </pre>
            </div>
          ) : (
            <Typography.Paragraph>Ошибка: {result.error}</Typography.Paragraph>
          )}
        </div>
      )}
    </section>
  );
};
