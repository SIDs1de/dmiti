import axios, { type AxiosInstance } from "axios";
import type {
  Integer,
  IntegerAbsZNResponse,
  IntegerAddZZZRequest,
  IntegerAddZZZResponse,
  IntegerDivZZZRequest,
  IntegerDivZZZResponse,
  IntegerModZZZRequest,
  IntegerModZZZResponse,
  IntegerMulZMZResponse,
  IntegerMulZZZRequest,
  IntegerMulZZZResponse,
  IntegerPozZDResponse,
  IntegerSubZZZRequest,
  IntegerSubZZZResponse,
  IntegerTransZNResponse,
  Natural,
  NaturalAdd1NNResponse,
  NaturalAddNNNRequest,
  NaturalAddNNNResponse,
  NaturalComNNDRequest,
  NaturalComNNDResponse,
  NaturalDivNNDKRequest,
  NaturalDivNNDKResponse,
  NaturalDivNNNRequest,
  NaturalDivNNNResponse,
  NaturalGcfNNNRequest,
  NaturalGcfNNNResponse,
  NaturalLcmNNNRequest,
  NaturalLcmNNNResponse,
  NaturalModNNNRequest,
  NaturalModNNNResponse,
  NaturalMulNDNRequest,
  NaturalMulNDNResponse,
  NaturalMulNKNRequest,
  NaturalMulNKNResponse,
  NaturalMulNNNRequest,
  NaturalMulNNNResponse,
  NaturalNzerNBResponse,
  NaturalSubNDNNRequest,
  NaturalSubNDNNResponse,
  NaturalSubNNNRequest,
  NaturalSubNNNResponse,
  NaturalTransNZResponse,
  Rational,
  RationalAddQQQRequest,
  RationalAddQQQResponse,
  RationalDivQQQRequest,
  RationalDivQQQResponse,
  RationalIntQBResponse,
  RationalMulQQQRequest,
  RationalMulQQQResponse,
  RationalRedQQResponse,
  RationalSubQQQRequest,
  RationalSubQQQResponse,
  RationalTransQZResponse,
  RationalTransZQResponse,
} from "../types/api";

const API_BASE_URL = "http://localhost:5010/api";

const http: AxiosInstance = axios.create({
  baseURL: API_BASE_URL,
});

async function post<TReq, TRes>(url: string, data: TReq): Promise<TRes> {
  const resp = await http.post<TRes>(url, data);
  return resp.data;
}

export const algebraApi = {
  naturalComNND(request: NaturalComNNDRequest): Promise<NaturalComNNDResponse> {
    return post<NaturalComNNDRequest, NaturalComNNDResponse>("/natural/com_nn_d", request);
  },

  naturalNzerNB(request: Natural): Promise<NaturalNzerNBResponse> {
    return post<Natural, NaturalNzerNBResponse>("/natural/nzer_n_b", request);
  },

  naturalAdd1NN(request: Natural): Promise<NaturalAdd1NNResponse> {
    return post<Natural, NaturalAdd1NNResponse>("/natural/add_1n_n", request);
  },

  naturalAddNNN(request: NaturalAddNNNRequest): Promise<NaturalAddNNNResponse> {
    return post<NaturalAddNNNRequest, NaturalAddNNNResponse>("/natural/add_nn_n", request);
  },

  naturalSubNNN(request: NaturalSubNNNRequest): Promise<NaturalSubNNNResponse> {
    return post<NaturalSubNNNRequest, NaturalSubNNNResponse>("/natural/sub_nn_n", request);
  },

  naturalMulNDN(request: NaturalMulNDNRequest): Promise<NaturalMulNDNResponse> {
    return post<NaturalMulNDNRequest, NaturalMulNDNResponse>("/natural/mul_nd_n", request);
  },

  naturalMulNKN(request: NaturalMulNKNRequest): Promise<NaturalMulNKNResponse> {
    return post<NaturalMulNKNRequest, NaturalMulNKNResponse>("/natural/mul_nk_n", request);
  },

  naturalMulNNN(request: NaturalMulNNNRequest): Promise<NaturalMulNNNResponse> {
    return post<NaturalMulNNNRequest, NaturalMulNNNResponse>("/natural/mul_nn_n", request);
  },

  naturalSubNDNN(request: NaturalSubNDNNRequest): Promise<NaturalSubNDNNResponse> {
    return post<NaturalSubNDNNRequest, NaturalSubNDNNResponse>("/natural/sub_ndn_n", request);
  },

  naturalDivNNDK(request: NaturalDivNNDKRequest): Promise<NaturalDivNNDKResponse> {
    return post<NaturalDivNNDKRequest, NaturalDivNNDKResponse>("/natural/div_nn_dk", request);
  },

  naturalDivNNN(request: NaturalDivNNNRequest): Promise<NaturalDivNNNResponse> {
    return post<NaturalDivNNNRequest, NaturalDivNNNResponse>("/natural/div_nn_n", request);
  },

  naturalModNNN(request: NaturalModNNNRequest): Promise<NaturalModNNNResponse> {
    return post<NaturalModNNNRequest, NaturalModNNNResponse>("/natural/mod_nn_n", request);
  },

  naturalGcfNNN(request: NaturalGcfNNNRequest): Promise<NaturalGcfNNNResponse> {
    return post<NaturalGcfNNNRequest, NaturalGcfNNNResponse>("/natural/gcf_nn_n", request);
  },

  naturalLcmNNN(request: NaturalLcmNNNRequest): Promise<NaturalLcmNNNResponse> {
    return post<NaturalLcmNNNRequest, NaturalLcmNNNResponse>("/natural/lcm_nn_n", request);
  },

  integerAbsZN(request: Integer): Promise<IntegerAbsZNResponse> {
    return post<Integer, IntegerAbsZNResponse>("/integer/abs_z_n", request);
  },

  integerPozZD(request: Integer): Promise<IntegerPozZDResponse> {
    return post<Integer, IntegerPozZDResponse>("/integer/poz_z_d", request);
  },

  integerMulZMZ(request: Integer): Promise<IntegerMulZMZResponse> {
    return post<Integer, IntegerMulZMZResponse>("/integer/mul_zm_z", request);
  },

  naturalTransNZ(request: Natural): Promise<NaturalTransNZResponse> {
    return post<Natural, NaturalTransNZResponse>("/natural/trans_n_z", request);
  },

  integerTransZN(request: Integer): Promise<IntegerTransZNResponse> {
    return post<Integer, IntegerTransZNResponse>("/integer/trans_z_n", request);
  },

  integerAddZZZ(request: IntegerAddZZZRequest): Promise<IntegerAddZZZResponse> {
    return post<IntegerAddZZZRequest, IntegerAddZZZResponse>("/integer/add_zz_z", request);
  },

  integerSubZZZ(request: IntegerSubZZZRequest): Promise<IntegerSubZZZResponse> {
    return post<IntegerSubZZZRequest, IntegerSubZZZResponse>("/integer/sub_zz_z", request);
  },

  integerMulZZZ(request: IntegerMulZZZRequest): Promise<IntegerMulZZZResponse> {
    return post<IntegerMulZZZRequest, IntegerMulZZZResponse>("/integer/mul_zz_z", request);
  },

  integerDivZZZ(request: IntegerDivZZZRequest): Promise<IntegerDivZZZResponse> {
    return post<IntegerDivZZZRequest, IntegerDivZZZResponse>("/integer/div_zz_z", request);
  },

  integerModZZZ(request: IntegerModZZZRequest): Promise<IntegerModZZZResponse> {
    return post<IntegerModZZZRequest, IntegerModZZZResponse>("/integer/mod_zz_z", request);
  },

  rationalRedQQ(request: Rational): Promise<RationalRedQQResponse> {
    return post<Rational, RationalRedQQResponse>("/rational/red_q_q", request);
  },

  rationalIntQB(request: Rational): Promise<RationalIntQBResponse> {
    return post<Rational, RationalIntQBResponse>("/rational/int_q_b", request);
  },

  rationalTransZQ(request: Integer): Promise<RationalTransZQResponse> {
    return post<Integer, RationalTransZQResponse>("/rational/trans_z_q", request);
  },

  rationalTransQZ(request: Rational): Promise<RationalTransQZResponse> {
    return post<Rational, RationalTransQZResponse>("/rational/trans_q_z", request);
  },

  rationalAddQQQ(request: RationalAddQQQRequest): Promise<RationalAddQQQResponse> {
    return post<RationalAddQQQRequest, RationalAddQQQResponse>("/rational/add_qq_q", request);
  },

  rationalSubQQQ(request: RationalSubQQQRequest): Promise<RationalSubQQQResponse> {
    return post<RationalSubQQQRequest, RationalSubQQQResponse>("/rational/sub_qq_q", request);
  },

  rationalMulQQQ(request: RationalMulQQQRequest): Promise<RationalMulQQQResponse> {
    return post<RationalMulQQQRequest, RationalMulQQQResponse>("/rational/mul_qq_q", request);
  },

  rationalDivQQQ(request: RationalDivQQQRequest): Promise<RationalDivQQQResponse> {
    return post<RationalDivQQQRequest, RationalDivQQQResponse>("/rational/div_qq_q", request);
  },
};
