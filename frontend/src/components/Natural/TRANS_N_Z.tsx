import { useState } from "react";
import type { NaturalTransNZResponse } from "../../types/api";
import { algebraApi } from "../../services/api";
import { Button, InputNumber, Typography } from "antd";

export const TRANS_N_Z = () => {
  const [number, setNumber] = useState<string | null>(null);

  const [result, setResult] = useState<NaturalTransNZResponse | null>(null);
  const [loading, setLoading] = useState(false);

  const handleClick = async () => {
    setLoading(true);
    try {
      if (number === null) {
        throw new Error("Введите натуральное число");
      }
      const response = await algebraApi.naturalTransNZ({
        digits: String(number).split("").map(Number),
      });
      setResult(response);
    } catch (error) {
      console.error("Failed:", error);
      setResult({
        success: false,
        result: { sign: 0, absolute: [], string: "" },
        error: (error as Error).message,
      });
    }
    setLoading(false);
  };

  return (
    <section>
      <Typography.Title level={2}>TRANS_N_Z: Преобразование натурального в целое</Typography.Title>
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
        Преобразовать
      </Button>

      {result && (
        <div>
          <Typography.Title level={3}>Результат преобразования:</Typography.Title>
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
