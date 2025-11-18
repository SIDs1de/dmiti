import { useState } from "react";
import { algebraApi } from "../../services/api";
import { Button, InputNumber, Typography } from "antd";
import type { NaturalSubNNNResponse } from "../../types/api";

export const SUB_NN_N = () => {
  const [firstNumber, setFirstNumber] = useState<string | null>(null);
  const [secondNumber, setSecondNumber] = useState<string | null>(null);

  const [result, setResult] = useState<NaturalSubNNNResponse | null>(null);
  const [loading, setLoading] = useState(false);

  const handleClick = async () => {
    setLoading(true);
    try {
      if (firstNumber === null || secondNumber === null) {
        throw new Error("Введите два натуральных числа");
      }
      if (firstNumber < secondNumber) {
        throw new Error("Первое число должно быть больше или равно второму");
      }
      const response = await algebraApi.naturalSubNNN({
        a: { digits: String(firstNumber).split("").map(Number) },
        b: { digits: String(secondNumber).split("").map(Number) },
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
        SUB_NN_N: Вычитание из первого большего натурального числа второго меньшего или равного
      </Typography.Title>
      <label>
        <Typography.Text>Введите первое натуральное число:</Typography.Text>
        <InputNumber
            maxLength={12}
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
            maxLength={12}
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
        Вычесть
      </Button>

      {result && (
        <div>
          <Typography.Title level={3}>Результат вычитания:</Typography.Title>
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
