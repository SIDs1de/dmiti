import "normalize.css";
import styles from "./index.module.scss";
import "./App.scss";
import { Natural } from "./components/Natural";
import { Integer } from "./components/Integer";
import { Select, Typography } from "antd";
import { useState, type ReactNode } from "react";

type ComponentType = "natural" | "integer";

const options = [
  {
    value: "natural",
    label: "Натуральные числа",
  },
  {
    value: "integer",
    label: "Целые числа",
  },
];

const componentMap: Record<ComponentType, ReactNode> = {
  natural: <Natural />,
  integer: <Integer />,
};

const App: React.FC = () => {
  const [selectedType, setSelectedType] = useState<ComponentType>("natural");

  return (
    <div className={styles.container}>
      <Typography.Paragraph>Выбрать раздел:</Typography.Paragraph>
      <Select
        value={selectedType}
        onChange={(newValue) => setSelectedType(newValue as ComponentType)}
        options={options}
        style={{ width: 300 }}
      />
      {componentMap[selectedType]}
    </div>
  );
};

export default App;
