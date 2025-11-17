export interface Natural {
  digits: number[];
}

export interface NaturalComNNDRequest {
  a: Natural;
  b: Natural;
}

export interface NaturalComNNDResponse {
  success: boolean;
  result: number;
  description: string;
  error?: string;
}

export interface NaturalNzerNBResponse {
  success: boolean;
  result: number;
  description: string;
  error?: string;
}

export interface NaturalAdd1NNResponse {
  success: boolean;
  result: {
    digits: number[];
    string: string;
  };
  error?: string;
}

export interface NaturalAddNNNRequest {
  a: Natural;
  b: Natural;
}

export interface NaturalAddNNNResponse {
  success: boolean;
  result: {
    digits: number[];
    string: string;
  };
  error?: string;
}

export interface NaturalSubNNNRequest {
  a: Natural;
  b: Natural;
}

export interface NaturalSubNNNResponse {
  success: boolean;
  result: {
    digits: number[];
    string: string;
  };
  error?: string;
}

export interface NaturalMulNDNRequest {
  number: Natural;
  digit: number;
}

export interface NaturalMulNDNResponse {
  success: boolean;
  result: {
    digits: number[];
    string: string;
  };
  error?: string;
}

export interface NaturalMulNKNRequest {
  number: Natural;
  k: number;
}

export interface NaturalMulNKNResponse {
  success: boolean;
  result: {
    digits: number[];
    string: string;
  };
  error?: string;
}

export interface NaturalMulNNNRequest {
  a: Natural;
  b: Natural;
}

export interface NaturalMulNNNResponse {
  success: boolean;
  result: {
    digits: number[];
    string: string;
  };
  error?: string;
}

export interface NaturalSubNDNNRequest {
  a: Natural;
  b: Natural;
  digit: number;
}

export interface NaturalSubNDNNResponse {
  success: boolean;
  result: {
    digits: number[];
    string: string;
  };
  error?: string;
}

export interface NaturalDivNNDKRequest {
  a: Natural;
  b: Natural;
  k: number;
}

export interface NaturalDivNNDKResponse {
  success: boolean;
  result: number;
  error?: string;
}

export interface NaturalDivNNNRequest {
  a: Natural;
  b: Natural;
}

export interface NaturalDivNNNResponse {
  success: boolean;
  result: Natural;
  error?: string;
}

export interface NaturalModNNNRequest {
  a: Natural;
  b: Natural;
}

export interface NaturalModNNNResponse {
  success: boolean;
  result: Natural;
  error?: string;
}

export interface NaturalGcfNNNRequest {
  a: Natural;
  b: Natural;
}

export interface NaturalGcfNNNResponse {
  success: boolean;
  result: Natural;
  error?: string;
}

export interface NaturalLcmNNNRequest {
  a: Natural;
  b: Natural;
}

export interface NaturalLcmNNNResponse {
  success: boolean;
  result: Natural;
  error?: string;
}
