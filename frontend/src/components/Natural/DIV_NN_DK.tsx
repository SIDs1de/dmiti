import { useState } from "react";
import { algebraApi } from "../../services/api";
import { Button, InputNumber, Typography } from "antd";
import type { NaturalDivNNDKResponse } from "../../types/api";

export const DIV_NN_DK = () => {
  const [firstNumber, setFirstNumber] = useState<string | null>(null);
  const [secondNumber, setSecondNumber] = useState<string | null>(null);
  const [digit, setDigit] = useState<string | null>(null);

  const [result, setResult] = useState<NaturalDivNNDKResponse | null>(null);
  const [loading, setLoading] = useState(false);

  const handleClick = async () => {
    setLoading(true);
    try {
      if (firstNumber === null || secondNumber === null || digit === null) {
        throw new Error("Введите два натуральных числа и позицию.");
      }
      const response = await algebraApi.naturalDivNNDK({
        a: { digits: String(firstNumber).split("").map(Number) },
        b: { digits: String(secondNumber).split("").map(Number) },
        k: Number(digit),
      });
      setResult(response);
    } catch (error) {
      console.error("Failed:", error);
      setResult({
        success: false,
        result: -1,
        error: (error as Error).message,
      });
    }
    setLoading(false);
  };

  return (
    <section>
      <Typography.Title level={2}>
        DIV_NN_Dk: Вычисление первой цифры деления большего натурального на меньшее, домноженное на
        10^k,где k - номер позиции этой цифры (номер считается с нуля)
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
      <label>
        <Typography.Text>Введите позицию (k):</Typography.Text>
        <InputNumber
          precision={0}
          min={"0"}
          max={secondNumber ? String(secondNumber.length - 1) : ""}
          value={digit}
          onChange={(value) => setDigit(value)}
          placeholder="Позиция"
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
            <Typography.Paragraph>Результат: {result.result}</Typography.Paragraph>
          ) : (
            <Typography.Paragraph>Ошибка: {result.error}</Typography.Paragraph>
          )}
        </div>
      )}
    </section>
  );
};
