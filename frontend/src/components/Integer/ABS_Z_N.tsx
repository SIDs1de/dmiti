import { useState } from "react";
import type { IntegerAbsZNResponse } from "../../types/api";
import { algebraApi } from "../../services/api";
import { Button, InputNumber, Typography } from "antd";

export const ABS_Z_N = () => {
  const [number, setNumber] = useState<string | null>(null);

  const [result, setResult] = useState<IntegerAbsZNResponse | null>(null);
  const [loading, setLoading] = useState(false);

  const handleClick = async () => {
    setLoading(true);
    try {
      if (number === null) {
        throw new Error("Введите целое число");
      }
      const response = await algebraApi.integerAbsZN({
        sign: Number(number) >= 0 ? 0 : 1,
        absolute: Math.abs(Number(number)),
      });
      setResult(response);
    } catch (error) {
      console.error("Failed:", error);
      setResult({
        success: false,
        result: { digits: [], string: "" },
        error: (error as Error).message,
      });
    }
    setLoading(false);
  };

  return (
    <section>
      <Typography.Title level={2}>
        ABS_Z_N: Абсолютная величина числа, результат - натуральное
      </Typography.Title>
      <label>
        <Typography.Text>Введите целое число:</Typography.Text>
        <InputNumber
            maxLength={12}
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
        Вычислить
      </Button>

      {result && (
        <div>
          <Typography.Title level={3}>Результат вычисления:</Typography.Title>
          {result.success ? (
            <Typography.Paragraph>
              Результат: {JSON.stringify(result.result.digits)} ({result.result.string})
            </Typography.Paragraph>
          ) : (
            <Typography.Paragraph>Ошибка: {result.error}</Typography.Paragraph>
          )}
        </div>
      )}
    </section>
  );
};
