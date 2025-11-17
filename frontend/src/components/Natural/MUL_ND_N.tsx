import { useState } from "react";
import { algebraApi } from "../../services/api";
import { Button, InputNumber, Typography } from "antd";
import type { NaturalMulNDNResponse } from "../../types/api";

export const MUL_ND_N = () => {
  const [firstNumber, setFirstNumber] = useState<string | null>(null);
  const [secondNumber, setSecondNumber] = useState<string | null>(null);

  const [result, setResult] = useState<NaturalMulNDNResponse | null>(null);
  const [loading, setLoading] = useState(false);

  const handleClick = async () => {
    setLoading(true);
    try {
      if (firstNumber === null || secondNumber === null) {
        throw new Error("Введите натуральное число и цифру от 0 до 9");
      }
      const response = await algebraApi.naturalMulNDN({
        number: { digits: String(firstNumber).split("").map(Number) },
        digit: Number(secondNumber),
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
      <Typography.Title level={2}>MUL_ND_N: Умножение натурального числа на цифру</Typography.Title>
      <label>
        <Typography.Text>Введите натуральное число:</Typography.Text>
        <InputNumber
          min={"0"}
          value={firstNumber}
          onChange={(value) => setFirstNumber(value)}
          placeholder="Натуральное число"
        />
      </label>
      <label>
        <Typography.Text>Введите цифру от 0 до 9:</Typography.Text>
        <InputNumber
          min={"0"}
          max={"9"}
          value={secondNumber}
          onChange={(value) => setSecondNumber(value)}
          placeholder="Цифра"
        />
      </label>
      <Button
        onClick={handleClick}
        disabled={loading}
      >
        Умножить
      </Button>

      {result && (
        <div>
          <Typography.Title level={3}>Результат умножения:</Typography.Title>
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
