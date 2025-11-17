import { InputNumber } from "antd";
import styles from "./index.module.scss";

type RationalInputProps = {
  numerator: string | null;
  denominator: string | null;
  onNumeratorChange: (value: string | null) => void;
  onDenominatorChange: (value: string | null) => void;
};

export const RationalInput = ({
  numerator,
  denominator,
  onNumeratorChange,
  onDenominatorChange,
}: RationalInputProps) => {
  return (
    <div className={styles.root}>
      <InputNumber
        className={styles.input}
        precision={0}
        value={numerator}
        onChange={onNumeratorChange}
        placeholder="Целое"
      />
      <InputNumber
        className={styles.input}
        precision={0}
        min={"1"}
        value={denominator}
        onChange={onDenominatorChange}
        placeholder="Натуральное"
      />
    </div>
  );
};
