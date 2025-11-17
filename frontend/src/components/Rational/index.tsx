import { List, Typography } from "antd";
import { RED_Q_Q } from "./RED_Q_Q";
import { INT_Q_B } from "./INT_Q_B";
import { TRANS_Z_Q } from "./TRANS_Z_Q";
import { TRANS_Q_Z } from "./TRANS_Q_Z";
import { ADD_QQ_Q } from "./ADD_QQ_Q";
import { SUB_QQ_Q } from "./SUB_QQ_Q";
import { MUL_QQ_Q } from "./MUL_QQ_Q";
import { DIV_QQ_Q } from "./DIV_QQ_Q";

const sections = [
  <RED_Q_Q />,
  <INT_Q_B />,
  <TRANS_Z_Q />,
  <TRANS_Q_Z />,
  <ADD_QQ_Q />,
  <SUB_QQ_Q />,
  <MUL_QQ_Q />,
  <DIV_QQ_Q />,
];

export const Rational = () => {
  return (
    <section>
      <Typography.Title level={1}>Операции с рациональными числами</Typography.Title>
      <div className={"section"}>
        <List bordered>
          {sections.map((SectionComponent, index) => (
            <List.Item key={index}>{SectionComponent}</List.Item>
          ))}
        </List>
      </div>
    </section>
  );
};
