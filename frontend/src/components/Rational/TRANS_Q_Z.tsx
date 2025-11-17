import { useState } from "react";
import type { RationalTransQZResponse } from "../../types/api";
import { algebraApi } from "../../services/api";
import { Button, Typography } from "antd";
import { RationalInput } from "../../shared/RationalInput";

export const TRANS_Q_Z = () => {
  const [numerator, setNumerator] = useState<string | null>(null);
  const [denominator, setDenominator] = useState<string | null>(null);

  const [result, setResult] = useState<RationalTransQZResponse | null>(null);
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
      if (+denominator !== 1) {
        throw new Error("Знаменатель должен быть равен 1 для преобразования в целое число");
      }

      const response = await algebraApi.rationalTransQZ({
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
          sign: 0,
          absolute: 0,
          string: "",
        },
        error: (error as Error).message,
      });
    }
    setLoading(false);
  };

  return (
    <section>
      <Typography.Title level={2}>
        TRANS_Q_Z: Преобразование сокращенного дробного в целое (если знаменатель равен 1)
      </Typography.Title>
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
        Преобразовать
      </Button>

      {result && (
        <div>
          <Typography.Title level={3}>Результат преобразования:</Typography.Title>
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
