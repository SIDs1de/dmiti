import { useState } from "react";
import { algebraApi } from "../../services/api";
import { Button, InputNumber, Typography } from "antd";
import type { NaturalMulNKNResponse } from "../../types/api";

export const MUL_NK_N = () => {
  const [firstNumber, setFirstNumber] = useState<string | null>(null);
  const [secondNumber, setSecondNumber] = useState<string | null>(null);

  const [result, setResult] = useState<NaturalMulNKNResponse | null>(null);
  const [loading, setLoading] = useState(false);

  const handleClick = async () => {
    setLoading(true);
    try {
      if (firstNumber === null || secondNumber === null) {
        throw new Error("Введите два натуральных числа");
      }
      const response = await algebraApi.naturalMulNKN({
        number: { digits: String(firstNumber).split("").map(Number) },
        k: Number(secondNumber),
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
        MUL_Nk_N: Умножение натурального числа на 10^k, k-натуральное (не длинное)
      </Typography.Title>
      <label>
        <Typography.Text>Введите натуральное число:</Typography.Text>
        <InputNumber
          precision={0}
          min={"0"}
          value={firstNumber}
          onChange={(value) => setFirstNumber(value)}
          placeholder="Натуральное число"
        />
      </label>
      <label>
        <Typography.Text>Введите число (не длинное):</Typography.Text>
        <InputNumber
          precision={0}
          min={"0"}
          value={secondNumber}
          onChange={(value) => setSecondNumber(value)}
          placeholder="Число"
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
