import { useState } from "react";
import type { IntegerMulZMZResponse } from "../../types/api";
import { algebraApi } from "../../services/api";
import { Button, InputNumber, Typography } from "antd";

export const MUL_ZM_Z = () => {
  const [number, setNumber] = useState<string | null>(null);

  const [result, setResult] = useState<IntegerMulZMZResponse | null>(null);
  const [loading, setLoading] = useState(false);

  const handleClick = async () => {
    setLoading(true);
    try {
      if (number === null) {
        throw new Error("Введите целое число");
      }
      const response = await algebraApi.integerMulZMZ({
        sign: Number(number) >= 0 ? 0 : 1,
        absolute: Math.abs(Number(number)),
      });
      setResult(response);
    } catch (error) {
      console.error("Failed:", error);
      setResult({
        success: false,
        result: { sign: 0, digits: [], string: "" },
        error: (error as Error).message,
      });
    }
    setLoading(false);
  };

  return (
    <section>
      <Typography.Title level={2}>MUL_ZM_Z: Умножение целого на (-1)</Typography.Title>
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
