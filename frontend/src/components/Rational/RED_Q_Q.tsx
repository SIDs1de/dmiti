import { useState } from "react";
import type { RationalRedQQResponse } from "../../types/api";
import { algebraApi } from "../../services/api";
import { Button, Typography } from "antd";
import { RationalInput } from "../../shared/RationalInput";

export const RED_Q_Q = () => {
  const [numerator, setNumerator] = useState<string | null>(null);
  const [denominator, setDenominator] = useState<string | null>(null);

  const [result, setResult] = useState<RationalRedQQResponse | null>(null);
  const [loading, setLoading] = useState(false);

  const handleClick = async () => {
    setLoading(true);
    try {
      if (numerator === null || denominator === null) {
        throw new Error("Введите числитель и знаменатель");
      }
      if (+denominator === 0) {
        throw new Error("Знаменатель не может быть нулём");
      }

      const response = await algebraApi.rationalRedQQ({
        numerator: {
          sign: Number(numerator) >= 0 ? 0 : 1,
          absolute: Math.abs(Number(numerator)),
        },
        denominator: {
          digits: String(denominator)
            .split("")
            .map((d) => Number(d)),
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
            digits: [],
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
      <Typography.Title level={2}>RED_Q_Q: Сокращение дроби</Typography.Title>
      <label>
        <Typography.Text>Введите дробь:</Typography.Text>
        <RationalInput
          numerator={numerator}
          denominator={denominator}
          onNumeratorChange={setNumerator}
          onDenominatorChange={setDenominator}
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
