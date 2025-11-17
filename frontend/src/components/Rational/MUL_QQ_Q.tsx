import { useState } from "react";
import type { RationalMulQQQResponse } from "../../types/api";
import { algebraApi } from "../../services/api";
import { Button, Typography } from "antd";
import { RationalInput } from "../../shared/RationalInput";

export const MUL_QQ_Q = () => {
  const [numeratorA, setNumeratorA] = useState<string | null>(null);
  const [denominatorA, setDenominatorA] = useState<string | null>(null);
  const [numeratorB, setNumeratorB] = useState<string | null>(null);
  const [denominatorB, setDenominatorB] = useState<string | null>(null);

  const [result, setResult] = useState<RationalMulQQQResponse | null>(null);
  const [loading, setLoading] = useState(false);

  const handleClick = async () => {
    setLoading(true);
    try {
      if (
        numeratorA === null ||
        denominatorA === null ||
        numeratorB === null ||
        denominatorB === null
      ) {
        throw new Error("Введите числитель и знаменатель");
      }
      if (+denominatorA === 0 || +denominatorB === 0) {
        throw new Error("Знаменатель не может быть нулём");
      }

      const response = await algebraApi.rationalMulQQQ({
        a: {
          numerator: {
            sign: Number(numeratorA) >= 0 ? 0 : 1,
            absolute: Math.abs(Number(numeratorA)),
          },
          denominator: {
            digits: String(denominatorA)
              .split("")
              .map((d) => Number(d)),
          },
        },
        b: {
          numerator: {
            sign: Number(numeratorB) >= 0 ? 0 : 1,
            absolute: Math.abs(Number(numeratorB)),
          },
          denominator: {
            digits: String(denominatorB)
              .split("")
              .map((d) => Number(d)),
          },
        },
      });
      setResult(response);
    } catch (error) {
      console.error("Failed:", error);
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
          string: "",
        },
        error: (error as Error).message,
      });
    }
    setLoading(false);
  };

  return (
    <section>
      <Typography.Title level={2}>MUL_QQ_Q: Умножение дробей</Typography.Title>
      <label>
        <Typography.Text>Введите первую дробь:</Typography.Text>
        <RationalInput
          numerator={numeratorA}
          denominator={denominatorA}
          onNumeratorChange={setNumeratorA}
          onDenominatorChange={setDenominatorA}
        />
      </label>
      <label>
        <Typography.Text>Введите вторую дробь:</Typography.Text>
        <RationalInput
          numerator={numeratorB}
          denominator={denominatorB}
          onNumeratorChange={setNumeratorB}
          onDenominatorChange={setDenominatorB}
        />
      </label>
      <Button
        onClick={handleClick}
        disabled={loading}
      >
        Вычислить
      </Button>

      {result && (
        <div>
          <Typography.Title level={3}>Результат вычисления:</Typography.Title>
          {result.success ? (
            <Typography.Paragraph>
              Результат: {JSON.stringify(result.result)} ({result.result.string})
            </Typography.Paragraph>
          ) : (
            <Typography.Paragraph>Ошибка: {result.error}</Typography.Paragraph>
          )}
        </div>
      )}
    </section>
  );
};
