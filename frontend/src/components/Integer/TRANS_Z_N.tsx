import { useState } from "react";
import type { IntegerTransZNResponse } from "../../types/api";
import { algebraApi } from "../../services/api";
import { Button, InputNumber, Typography } from "antd";

export const TRANS_Z_N = () => {
  const [number, setNumber] = useState<string | null>(null);

  const [result, setResult] = useState<IntegerTransZNResponse | null>(null);
  const [loading, setLoading] = useState(false);

  const handleClick = async () => {
    setLoading(true);
    try {
      if (number === null) {
        throw new Error("Введите целое неотрицательное число");
      }
      const response = await algebraApi.integerTransZN({
        sign: Number(number) >= 0 ? 0 : 1,
        absolute: Math.abs(Number(number)),
      });
      setResult(response);
    } catch (error) {
      console.error("Failed:", error);
      setResult({
        success: false,
        result: {
          digits: [],
        },
        error: (error as Error).message,
      });
    }
    setLoading(false);
  };

  return (
    <section>
      <Typography.Title level={2}>
        TRANS_Z_N: Преобразование целого неотрицательного в натуральное
      </Typography.Title>
      <label>
        <Typography.Text>Введите целое неотрицательное число:</Typography.Text>
        <InputNumber
            maxLength={12}
          precision={0}
          min={"0"}
          value={number}
          onChange={(value) => setNumber(value)}
          placeholder="Целое неотрицательное число"
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
              Результат: {JSON.stringify(result.result.digits)} ({result.result.digits})
            </Typography.Paragraph>
          ) : (
            <Typography.Paragraph>Ошибка: {result.error}</Typography.Paragraph>
          )}
        </div>
      )}
    </section>
  );
};
