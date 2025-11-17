import { useState } from "react";
import type { PolynomialLedPQResponse, Rational, ZeroOrOne } from "../../types/api";
import { algebraApi } from "../../services/api";
import { Button, Typography } from "antd";
import { PolynomialInput, type Monomial } from "../../shared/PolynomialInput";

export const LED_P_Q = () => {
  const [polynomial, setPolynomial] = useState<Monomial[]>([
    {
      coefficient: {
        numerator: null,
        denominator: null,
      },
      degree: null,
    },
  ]);

  const [result, setResult] = useState<PolynomialLedPQResponse | null>(null);
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

      const response = await algebraApi.polynomialLedPQ({
        polynomial: poly,
      });

      setResult(response);
    } catch (error) {
      console.error("Failed:", error);
      setError((error as Error).message);
      setResult({
        success: false,
        result: {
          numerator: {
            sign: 0,
            absolute: 0,
          },
          denominator: {
            digits: [1],
          },
        },
        error: (error as Error).message,
      });
    }

    setLoading(false);
  };

  const hasEmptyFields = () => {
    return polynomial.some(
      (monomial) =>
        monomial.coefficient.numerator === null ||
        monomial.coefficient.denominator === null ||
        monomial.degree === null,
    );
  };

  return (
    <section>
      <Typography.Title level={2}>LED_P_Q: Старший коэффициент многочлена</Typography.Title>

      <div style={{ marginBottom: "24px" }}>
        <Typography.Text strong>Полином:</Typography.Text>
        <PolynomialInput
          value={polynomial}
          onChange={setPolynomial}
        />
      </div>

      <Button
        onClick={handleClick}
        disabled={loading || hasEmptyFields()}
        style={{ marginBottom: "16px" }}
      >
        Получить старший коэффициент
      </Button>

      {error && <Typography.Paragraph>Ошибка: {error}</Typography.Paragraph>}

      {result && (
        <div>
          <Typography.Title level={3}>Старший коэффициент:</Typography.Title>
          {result.success ? (
            <div>
              <Typography.Paragraph>
                <strong>Числитель:</strong> {result.result.numerator.sign === 0 ? "" : "-"}
                {result.result.numerator.absolute}
              </Typography.Paragraph>
              <Typography.Paragraph>
                <strong>Знаменатель:</strong> {result.result.denominator.digits.join("")}
              </Typography.Paragraph>
              <Typography.Paragraph>
                <strong>Дробь:</strong> {result.result.numerator.sign === 0 ? "" : "-"}
                {result.result.numerator.absolute}/{result.result.denominator.digits.join("")}
              </Typography.Paragraph>
            </div>
          ) : (
            <Typography.Paragraph>Ошибка: {result.error}</Typography.Paragraph>
          )}
        </div>
      )}
    </section>
  );
};
