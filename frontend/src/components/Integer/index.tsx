import { List, Typography } from "antd";
import { ABS_Z_N } from "./ABS_Z_N";
import { POZ_Z_D } from "./POS_Z_D";
import { MUL_ZM_Z } from "./MUL_ZM_Z";
import { TRANS_Z_N } from "./TRANS_Z_N";
import { ADD_ZZ_Z } from "./ADD_ZZ_Z";
import { SUB_ZZ_Z } from "./SUB_ZZ_Z";
import { MUL_ZZ_Z } from "./MUL_ZZ_Z";
import { DIV_ZZ_Z } from "./DIV_ZZ_Z";
import { MOD_ZZ_Z } from "./MOD_ZZ_Z";

const sections = [
  <ABS_Z_N />,
  <POZ_Z_D />,
  <MUL_ZM_Z />,
  <TRANS_Z_N />,
  <ADD_ZZ_Z />,
  <SUB_ZZ_Z />,
  <MUL_ZZ_Z />,
  <DIV_ZZ_Z />,
  <MOD_ZZ_Z />,
];

export const Integer = () => {
  return (
    <section>
      <Typography.Title level={1}>Операции с целыми числами</Typography.Title>
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
