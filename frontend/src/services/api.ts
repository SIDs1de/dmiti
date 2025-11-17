import axios, { type AxiosInstance } from "axios";
import type {
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
};
