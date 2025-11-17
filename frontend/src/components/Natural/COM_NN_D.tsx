import { useState } from "react";
import type { NaturalComNNDResponse } from "../../types/api";
import { algebraApi } from "../../services/api";
import { Button, InputNumber, Typography } from "antd";

export const COM_NN_D = () => {
  const [firstNumber, setFirstNumber] = useState<string | null>(null);
  const [secondNumber, setSecondNumber] = useState<string | null>(null);

  const [result, setResult] = useState<NaturalComNNDResponse | null>(null);
  const [loading, setLoading] = useState(false);

  const handleClick = async () => {
    setLoading(true);
    try {
      if (firstNumber === null || secondNumber === null) {
        throw new Error("Введите два натуральных числа");
      }
      const response = await algebraApi.naturalComNND({
        a: { digits: String(firstNumber).split("").map(Number) },
        b: { digits: String(secondNumber).split("").map(Number) },
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
        COM_NN_D: Сравнение натуральных чисел: 2 - если первое больше второго, 0, если равно, 1
        иначе.
      </Typography.Title>
      <label>
        <Typography.Text>Введите первое натуральное число:</Typography.Text>
        <InputNumber
          precision={0}
          min={"0"}
          value={firstNumber}
          onChange={(value) => setFirstNumber(value)}
          placeholder="Натуральное число"
        />
      </label>
      <label>
        <Typography.Text>Введите второе натуральное число:</Typography.Text>
        <InputNumber
          precision={0}
          min={"0"}
          value={secondNumber}
          onChange={(value) => setSecondNumber(value)}
          placeholder="Натуральное число"
        />
      </label>
      <Button
        onClick={handleClick}
        disabled={loading}
      >
        Сравнить
      </Button>

      {result && (
        <div>
          <Typography.Title level={3}>Результат сравнения:</Typography.Title>
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
