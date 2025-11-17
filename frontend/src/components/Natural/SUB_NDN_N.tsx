import { useState } from "react";
import { algebraApi } from "../../services/api";
import { Button, InputNumber, Typography } from "antd";
import type { NaturalSubNDNNResponse } from "../../types/api";

export const SUB_NDN_N = () => {
  const [firstNumber, setFirstNumber] = useState<string | null>(null);
  const [secondNumber, setSecondNumber] = useState<string | null>(null);
  const [digit, setDigit] = useState<string | null>(null);

  const [result, setResult] = useState<NaturalSubNDNNResponse | null>(null);
  const [loading, setLoading] = useState(false);

  const handleClick = async () => {
    setLoading(true);
    try {
      if (firstNumber === null || secondNumber === null || digit === null) {
        throw new Error("Введите два натуральных числа и цифру.");
      }
      if (+firstNumber < +secondNumber * +digit) {
        throw new Error("Результат вычитания будет отрицательным.");
      }
      const response = await algebraApi.naturalSubNDNN({
        a: { digits: String(firstNumber).split("").map(Number) },
        b: { digits: String(secondNumber).split("").map(Number) },
        digit: Number(digit),
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
        SUB_NDN_N: Вычитание из натурального другого натурального, умноженного на цифру для случая с
        неотрицательным результатом
      </Typography.Title>
      <label>
        <Typography.Text>Введите первое натуральное число:</Typography.Text>
        <InputNumber
          min={"0"}
          value={firstNumber}
          onChange={(value) => setFirstNumber(value)}
          placeholder="Натуральное число"
        />
      </label>
      <label>
        <Typography.Text>Введите второе натуральное число:</Typography.Text>
        <InputNumber
          min={"0"}
          value={secondNumber}
          onChange={(value) => setSecondNumber(value)}
          placeholder="Натуральное число"
        />
      </label>
      <label>
        <Typography.Text>Введите цифру от 0 до 9:</Typography.Text>
        <InputNumber
          min={"0"}
          max={"9"}
          value={digit}
          onChange={(value) => setDigit(value)}
          placeholder="Цифра"
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
