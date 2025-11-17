import { useState } from "react";
import type { PolynomialFacPQResponse, Rational, ZeroOrOne } from "../../types/api";
import { algebraApi } from "../../services/api";
import { Button, Typography } from "antd";
import { PolynomialInput, type Monomial } from "../../shared/PolynomialInput";
import { AxiosError } from "axios";

export const FAC_P_Q = () => {
  const [polynomial, setPolynomial] = useState<Monomial[]>([
    {
      coefficient: {
        numerator: null,
        denominator: null,
      },
      degree: null,
    },
  ]);

  const [result, setResult] = useState<PolynomialFacPQResponse | null>(null);
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

      const response = await algebraApi.polynomialFacPQ({
        polynomial: poly,
      });

      setResult(response);
    } catch (error) {
      console.error("Failed:", error);

      let errorMessage = "Неизвестная ошибка";

      if (error instanceof AxiosError) {
        if (error.response?.data?.error) {
          errorMessage = error.response.data.error;
        } else if (error.response?.status === 500) {
          errorMessage = "Внутренняя ошибка сервера. Проверьте правильность введенных данных.";
        } else if (error.message) {
          errorMessage = error.message;
        }
      } else if (error instanceof Error) {
        errorMessage = error.message;
      }

      setError(errorMessage);
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
        error: errorMessage,
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
      <Typography.Title level={2}>
        FAC_P_Q: Вынесение из многочлена НОК знаменателей коэффициентов и НОД числителей
      </Typography.Title>

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
        Вычислить
      </Button>

      {error && (
        <Typography.Paragraph style={{ color: "#ff4d4f" }}>Ошибка: {error}</Typography.Paragraph>
      )}

      {result && (
        <div>
          <Typography.Title level={3}>Результат:</Typography.Title>
          {result.success ? (
            <div>
              <Typography.Paragraph>
                <strong>НОД числителей / НОК знаменателей:</strong>
              </Typography.Paragraph>
              <Typography.Paragraph>
                <strong>Числитель (НОД):</strong> {result.result.numerator.sign === 0 ? "" : "-"}
                {result.result.numerator.absolute}
              </Typography.Paragraph>
              <Typography.Paragraph>
                <strong>Знаменатель (НОК):</strong> {result.result.denominator.digits.join("")}
              </Typography.Paragraph>
              <Typography.Paragraph>
                <strong>Дробь:</strong> {result.result.numerator.sign === 0 ? "" : "-"}
                {result.result.numerator.absolute}/{result.result.denominator.digits.join("")}
              </Typography.Paragraph>
            </div>
          ) : (
            <Typography.Paragraph style={{ color: "#ff4d4f" }}>
              Ошибка: {result.error}
            </Typography.Paragraph>
          )}
        </div>
      )}
    </section>
  );
};
