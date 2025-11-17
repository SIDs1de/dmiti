import { useState } from "react";
import type { IntegerPozZDResponse } from "../../types/api";
import { algebraApi } from "../../services/api";
import { Button, InputNumber, Typography } from "antd";

export const POZ_Z_D = () => {
  const [number, setNumber] = useState<string | null>(null);

  const [result, setResult] = useState<IntegerPozZDResponse | null>(null);
  const [loading, setLoading] = useState(false);

  const handleClick = async () => {
    setLoading(true);
    try {
      if (number === null) {
        throw new Error("Введите целое число");
      }
      const response = await algebraApi.integerPozZD({
        sign: Number(number) >= 0 ? 0 : 1,
        absolute: Math.abs(Number(number)),
      });
      setResult(response);
    } catch (error) {
      console.error("Failed:", error);
      setResult({
        success: false,
        result: -1,
        description: "Ошибка при выполнении запроса",
        error: (error as Error).message,
      });
    }
    setLoading(false);
  };

  return (
    <section>
      <Typography.Title level={2}>
        POZ_Z_D: Определение положительности числа (2 - положительное, 0 — равное нулю, 1 -
        отрицательное)
      </Typography.Title>
      <label>
        <Typography.Text>Введите целое число:</Typography.Text>
        <InputNumber
          precision={0}
          value={number}
          onChange={(value) => setNumber(value)}
          placeholder="Целое число"
        />
      </label>
      <Button
        onClick={handleClick}
        disabled={loading}
      >
        Определить
      </Button>

      {result && (
        <div>
          <Typography.Title level={3}>Результат определения:</Typography.Title>
          {result.success ? (
            <Typography.Paragraph>
              Результат: {result.result} ({result.description})
            </Typography.Paragraph>
          ) : (
            <Typography.Paragraph>Ошибка: {result.error}</Typography.Paragraph>
          )}
        </div>
      )}
    </section>
  );
};
