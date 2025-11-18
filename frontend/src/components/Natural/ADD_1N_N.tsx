import { useState } from "react";
import type { NaturalAdd1NNResponse } from "../../types/api";
import { algebraApi } from "../../services/api";
import { Button, InputNumber, Typography } from "antd";

export const ADD_1N_N = () => {
  const [number, setNumber] = useState<string | null>(null);

  const [result, setResult] = useState<NaturalAdd1NNResponse | null>(null);
  const [loading, setLoading] = useState(false);

  const handleClick = async () => {
    setLoading(true);
    try {
      if (number === null) {
        throw new Error("Введите натуральное число");
      }
      const response = await algebraApi.naturalAdd1NN({
        digits: String(number).split("").map(Number),
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
      <Typography.Title level={2}>ADD_1N_N: Добавление 1 к натуральному числу</Typography.Title>
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
        Добавить
      </Button>

      {result && (
        <div>
          <Typography.Title level={3}>Результат добавления:</Typography.Title>
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
