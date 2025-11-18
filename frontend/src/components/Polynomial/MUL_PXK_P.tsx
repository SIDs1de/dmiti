import { useState } from "react";
import type { PolynomialMulPxkResponse, Rational, ZeroOrOne } from "../../types/api";
import { algebraApi } from "../../services/api";
import { Button, Typography, InputNumber } from "antd";
import { PolynomialInput, type Monomial } from "../../shared/PolynomialInput";

export const MUL_PXK_P = () => {
  const [polynomial, setPolynomial] = useState<Monomial[]>([
    {
      coefficient: {
        numerator: null,
        denominator: null,
      },
      degree: null,
    },
  ]);

  const [k, setK] = useState<string | null>(null);

  const [result, setResult] = useState<PolynomialMulPxkResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const uiToApiFormat = (uiPolynomial: typeof polynomial) => {
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
            sign: (numerator >= 0 ? 0 : 1) as ZeroOrOne,
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
      const poly = uiToApiFormat(polynomial);

      if (k === null) {
        throw new Error("Введите степень k");
      }

      const kNumber = Number(k);
      if (isNaN(kNumber) || kNumber < 0 || !Number.isInteger(kNumber)) {
        throw new Error("Степень k должна быть неотрицательным целым числом");
      }

      const naturalK = {
        digits: String(kNumber)
          .split("")
          .map((d) => Number(d)),
      };

      const response = await algebraApi.polynomialMulPxk({
        polynomial: poly,
        k: naturalK,
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
    const checkPolynomial = (poly: typeof polynomial) => {
      return poly.some(
        (monomial) =>
          monomial.coefficient.numerator === null ||
          monomial.coefficient.denominator === null ||
          monomial.degree === null,
      );
    };

    return checkPolynomial(polynomial) || k === null;
  };

  return (
    <section>
      <Typography.Title level={2}>
        MUL_Pxk_P: Умножение многочлена на x^k, k-натуральное или 0
      </Typography.Title>

      <div style={{ marginBottom: "24px" }}>
        <Typography.Text strong>Полином:</Typography.Text>
        <PolynomialInput
          value={polynomial}
          onChange={setPolynomial}
        />
      </div>

      <div style={{ marginBottom: "24px" }}>
        <Typography.Text strong>Степень k (натуральное число):</Typography.Text>
        <InputNumber
            maxLength={12}
          min={"0"}
          precision={0}
          value={k}
          onChange={setK}
          placeholder="Введите степень k"
          style={{ width: "100%" }}
        />
      </div>

      <Button
        onClick={handleClick}
        disabled={loading || hasEmptyFields()}
        style={{ marginBottom: "16px" }}
      >
        Вычислить произведение
      </Button>

      {error && <Typography.Paragraph>Ошибка: {error}</Typography.Paragraph>}

      {result && (
        <div>
          <Typography.Title level={3}>Результат умножения:</Typography.Title>
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
