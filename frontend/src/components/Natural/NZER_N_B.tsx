import { useState } from "react";
import type { NaturalComNNDResponse } from "../../types/api";
import { algebraApi } from "../../services/api";
import { Button, InputNumber, Typography } from "antd";

export const NZER_N_B = () => {
  const [number, setNumber] = useState<string | null>(null);

  const [result, setResult] = useState<NaturalComNNDResponse | null>(null);
  const [loading, setLoading] = useState(false);

  const handleClick = async () => {
    setLoading(true);
    try {
      if (number === null) {
        throw new Error("Введите натуральное число");
      }
      const response = await algebraApi.naturalNzerNB({
        digits: String(number).split("").map(Number),
      });
      setResult(response);
    } catch (error) {
      console.error("Failed:", error);
      setResult({
        success: false,
        result: -1,
        description: "Error",
        error: (error as Error).message,
      });
    }
    setLoading(false);
  };

  return (
    <section>
      <Typography.Title level={2}>
        NZER_N_B: Проверка на ноль: если число не равно нулю, то «да» иначе «нет»
      </Typography.Title>
      <label>
        <Typography.Text>Введите натуральное число:</Typography.Text>
        <InputNumber
            maxLength={12}
          precision={0}
          min={"0"}
          value={number}
          onChange={(value) => setNumber(value)}
          placeholder="Натуральное число"
        />
      </label>
      <Button
        onClick={handleClick}
        disabled={loading}
      >
        Проверить
      </Button>

      {result && (
        <div>
          <Typography.Title level={3}>Результат проверки:</Typography.Title>
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
