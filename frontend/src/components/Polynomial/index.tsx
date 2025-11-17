import { List, Typography } from "antd";
import { ADD_PP_P } from "./ADD_PP_P";
import { SUB_PP_P } from "./SUB_PP_P";
import { MUL_PQ_P } from "./MUL_PQ_P";
import { MUL_PXK_P } from "./MUL_PXK_P";
import { LED_P_Q } from "./LED_P_Q";
import { DEG_P_N } from "./DEG_P_N";
import { FAC_P_Q } from "./FAC_P_Q";
import { MUL_PP_P } from "./MUL_PP_P";
import { DIV_PP_P } from "./DIV_PP_P";
import { MOD_PP_P } from "./MOD_PP_P";
import { GCF_PP_P } from "./GCF_PP_P";
import { DER_P_P } from "./DER_P_P";
import { NMR_P_P } from "./NMR_P_P";

const sections = [
  <ADD_PP_P />,
  <SUB_PP_P />,
  <MUL_PQ_P />,
  <MUL_PXK_P />,
  <LED_P_Q />,
  <DEG_P_N />,
  <FAC_P_Q />,
  <MUL_PP_P />,
  <DIV_PP_P />,
  <MOD_PP_P />,
  <GCF_PP_P />,
  <DER_P_P />,
  <NMR_P_P />,
];

export const Polynomial = () => {
  return (
    <section>
      <Typography.Title level={1}>Операции с полиномами</Typography.Title>
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
