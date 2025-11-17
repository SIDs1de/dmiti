import { List, Typography } from "antd";
import { COM_NN_D } from "./COM_NN_D";
import { NZER_N_B } from "./NZER_N_B";
import { ADD_1N_N } from "./ADD_1N_N";
import { ADD_NN_N } from "./ADD_NN_N";
import { SUB_NN_N } from "./SUB_NN_N";
import { MUL_ND_N } from "./MUL_ND_N";
import { MUL_NK_N } from "./MUL_NK_N";
import { MUL_NN_N } from "./MUL_NN_N";
import { SUB_NDN_N } from "./SUB_NDN_N";
import { DIV_NN_DK } from "./DIV_NN_DK";
import { DIV_NN_N } from "./DIV_NN_N";
import { MOD_NN_N } from "./MOD_NN_N";
import { GCF_NN_N } from "./GCF_NN_N";
import { LCM_NN_N } from "./LCM_NN_N";
import { TRANS_N_Z } from "./TRANS_N_Z";

const sections = [
  <COM_NN_D />,
  <NZER_N_B />,
  <ADD_1N_N />,
  <ADD_NN_N />,
  <SUB_NN_N />,
  <MUL_ND_N />,
  <MUL_NK_N />,
  <MUL_NN_N />,
  <SUB_NDN_N />,
  <DIV_NN_DK />,
  <DIV_NN_N />,
  <MOD_NN_N />,
  <GCF_NN_N />,
  <LCM_NN_N />,
  <TRANS_N_Z />,
];

export const Natural = () => {
  return (
    <section>
      <Typography.Title level={1}>Операции с натуральными числами</Typography.Title>
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
