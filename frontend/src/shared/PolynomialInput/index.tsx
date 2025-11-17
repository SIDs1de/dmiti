import { Button, InputNumber } from "antd";
import { MinusCircleOutlined, PlusCircleOutlined } from "@ant-design/icons";
import styles from "./index.module.scss";
import { RationalInput } from "../RationalInput";

export interface Monomial {
  coefficient: {
    numerator: string | null;
    denominator: string | null;
  };
  degree: string | null;
}

interface PolynomialInputProps {
  value: Monomial[];
  onChange: (value: Monomial[]) => void;
}

export const PolynomialInput = ({ value, onChange }: PolynomialInputProps) => {
  const addMonomial = () => {
    const newMonomial: Monomial = {
      coefficient: {
        numerator: null,
        denominator: null,
      },
      degree: null,
    };
    onChange([...value, newMonomial]);
  };

  const removeMonomial = (index: number) => {
    const newValue = value.filter((_, i) => i !== index);
    onChange(newValue);
  };

  const updateCoefficient = (
    index: number,
    field: "numerator" | "denominator",
    newValue: string | null,
  ) => {
    const newValueArray = [...value];
    newValueArray[index] = {
      ...newValueArray[index],
      coefficient: {
        ...newValueArray[index].coefficient,
        [field]: newValue,
      },
    };
    onChange(newValueArray);
  };

  const updateDegree = (index: number, newDegree: string | null) => {
    const newValueArray = [...value];
    newValueArray[index] = {
      ...newValueArray[index],
      degree: newDegree,
    };
    onChange(newValueArray);
  };

  const isDegreeDuplicate = (currentIndex: number, degree: string | null): boolean => {
    if (!degree) return false;

    return value.some((monomial, index) => index !== currentIndex && monomial.degree === degree);
  };

  return (
    <div className={styles.polynomialRoot}>
      {value.map((monomial, index) => (
        <div
          key={index}
          className={styles.monomialRow}
        >
          <div className={styles.monomialContent}>
            <RationalInput
              numerator={monomial.coefficient.numerator}
              denominator={monomial.coefficient.denominator}
              onNumeratorChange={(val) => updateCoefficient(index, "numerator", val)}
              onDenominatorChange={(val) => updateCoefficient(index, "denominator", val)}
            />

            <span className={styles.xSymbol}>X</span>

            <InputNumber
              className={styles.degreeInput}
              precision={0}
              min={"0"}
              value={monomial.degree}
              onChange={(val) => updateDegree(index, val)}
              placeholder="Степень"
              status={isDegreeDuplicate(index, monomial.degree) ? "error" : ""}
            />

            <Button
              type="text"
              danger
              icon={<MinusCircleOutlined />}
              onClick={() => removeMonomial(index)}
              disabled={value.length <= 1}
              className={styles.removeButton}
            />
          </div>
        </div>
      ))}

      <Button
        type="dashed"
        icon={<PlusCircleOutlined />}
        onClick={addMonomial}
        className={styles.addButton}
        block
      >
        Добавить моном
      </Button>
    </div>
  );
};
