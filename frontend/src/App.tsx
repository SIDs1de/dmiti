import "normalize.css";
import styles from "./index.module.scss";
import "./App.scss";
import { Natural } from "./components/Natural";
import { Integer } from "./components/Integer";
import { Select, Typography } from "antd";
import { BrowserRouter, Navigate, Route, Routes, useLocation, useNavigate } from "react-router-dom";
import { Rational } from "./components/Rational";

type ComponentType = "natural" | "integer" | "rational" | "polynomial";

const options = [
  { value: "natural", label: "Натуральные числа" },
  { value: "integer", label: "Целые числа" },
  { value: "rational", label: "Рациональные числа" },
  { value: "polynomial", label: "Многочлены" },
];

const SelectorAndOutlet = () => {
  const navigate = useNavigate();
  const location = useLocation();

  const path = location.pathname.replace(/^\/+/, "");
  const selectedType = (
    ["natural", "integer", "rational", "polynomial"].includes(path)
      ? (path as ComponentType)
      : "natural"
  ) as ComponentType;

  const onChange = (newValue: string) => {
    const route = newValue === "natural" ? "/" : `/${newValue}`;
    navigate(route, { replace: false });
  };

  return (
    <div className={styles.container}>
      <Typography.Paragraph>Выбрать раздел:</Typography.Paragraph>
      <Select
        value={selectedType}
        onChange={(v) => onChange(v)}
        options={options}
        style={{ width: 300 }}
      />
      <Routes>
        <Route
          path="/"
          element={<Natural />}
        />
        <Route
          path="/natural"
          element={<Natural />}
        />
        <Route
          path="/integer"
          element={<Integer />}
        />
        <Route
          path="/rational"
          element={<Rational />}
        />
        <Route
          path="*"
          element={
            <Navigate
              to="/"
              replace
            />
          }
        />
      </Routes>
    </div>
  );
};

const App: React.FC = () => {
  return (
    <BrowserRouter>
      <SelectorAndOutlet />
    </BrowserRouter>
  );
};

export default App;
