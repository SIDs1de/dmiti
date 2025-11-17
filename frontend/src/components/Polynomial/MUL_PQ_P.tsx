import { useState } from "react";
import type { PolynomialMulPQResponse, Rational, ZeroOrOne } from "../../types/api";
import { algebraApi } from "../../services/api";
import { Button, Typography } from "antd";
import { PolynomialInput, type Monomial } from "../../shared/PolynomialInput";
import { RationalInput } from "../../shared/RationalInput";

export const MUL_PQ_P = () => {
  const [polynomial, setPolynomial] = useState<Monomial[]>([
    {
      coefficient: {
        numerator: null,
        denominator: null,
      },
      degree: null,
    },
  ]);

  const [rationalNumerator, setRationalNumerator] = useState<string | null>(null);
  const [rationalDenominator, setRationalDenominator] = useState<string | null>(null);

  const [result, setResult] = useState<PolynomialMulPQResponse | null>(null);
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

      if (rationalNumerator === null || rationalDenominator === null) {
        throw new Error("Введите числитель и знаменатель рационального числа");
      }

      if (+rationalDenominator === 0) {
        throw new Error("Знаменатель не может быть нулём");
      }

      const rational = {
        numerator: {
          sign: (Number(rationalNumerator) >= 0 ? 0 : 1) as ZeroOrOne,
          absolute: Math.abs(Number(rationalNumerator)),
        },
        denominator: {
          digits: String(rationalDenominator)
            .split("")
            .map((d) => Number(d)),
        },
      };

      const response = await algebraApi.polynomialMulPQ({
        polynomial: poly,
        rational: rational,
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

    return (
      checkPolynomial(polynomial) || rationalNumerator === null || rationalDenominator === null
    );
  };

  return (
    <section>
      <Typography.Title level={2}>
        MUL_PQ_P: Умножение многочлена на рациональное число
      </Typography.Title>

      <div style={{ marginBottom: "24px" }}>
        <Typography.Text strong>Полином:</Typography.Text>
        <PolynomialInput
          value={polynomial}
          onChange={setPolynomial}
        />
      </div>

      <div style={{ marginBottom: "24px" }}>
        <Typography.Text strong>Рациональное число:</Typography.Text>
        <RationalInput
          numerator={rationalNumerator}
          denominator={rationalDenominator}
          onNumeratorChange={setRationalNumerator}
          onDenominatorChange={setRationalDenominator}
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
