import { useState } from "react";
import type { IntegerSubZZZResponse } from "../../types/api";
import { algebraApi } from "../../services/api";
import { Button, InputNumber, Typography } from "antd";

export const SUB_ZZ_Z = () => {
  const [firstNumber, setFirstNumber] = useState<string | null>(null);
  const [secondNumber, setSecondNumber] = useState<string | null>(null);

  const [result, setResult] = useState<IntegerSubZZZResponse | null>(null);
  const [loading, setLoading] = useState(false);

  const handleClick = async () => {
    setLoading(true);
    try {
      if (firstNumber === null || secondNumber === null) {
        throw new Error("Введите два целых числа");
      }
      const response = await algebraApi.integerSubZZZ({
        a: {
          sign: Number(firstNumber) >= 0 ? 0 : 1,
          absolute: Math.abs(Number(firstNumber)),
        },
        b: {
          sign: Number(secondNumber) >= 0 ? 0 : 1,
          absolute: Math.abs(Number(secondNumber)),
        },
      });
      setResult(response);
    } catch (error) {
      console.error("Failed:", error);
      setResult({
        success: false,
        result: { absolute: 0, sign: 0, string: "" },
        error: (error as Error).message,
      });
    }
    setLoading(false);
  };

  return (
    <section>
      <Typography.Title level={2}>SUB_ZZ_Z: Вычитание целых чисел</Typography.Title>
      <label>
        <Typography.Text>Введите первое целое число:</Typography.Text>
        <InputNumber
          precision={0}
          value={firstNumber}
          onChange={(value) => setFirstNumber(value)}
          placeholder="Целое число"
        />
      </label>
      <label>
        <Typography.Text>Введите второе целое число:</Typography.Text>
        <InputNumber
          precision={0}
          value={secondNumber}
          onChange={(value) => setSecondNumber(value)}
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
