/* eslint-disable @typescript-eslint/no-empty-object-type */
export interface Natural {
  digits: number[];
}

export interface Integer {
  sign: ZeroOrOne;
  absolute: number;
}

export interface Rational {
  numerator: Integer;
  denominator: Natural;
}

export interface Polynomial {
  coefficients: { [degree: string]: Rational };
}

export interface PolynomialRepresentation {
  coefficients: { [degree: string]: Rational };
  degree: number;
  string: string;
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

export type ZeroOrOne = 0 | 1;

export interface IntegerAbsZNResponse {
  success: boolean;
  result: {
    digits: number[];
    string: string;
  };
  error?: string;
}

export interface IntegerPozZDResponse {
  success: boolean;
  result: -1 | 0 | 1 | 2;
  description: string;
  error?: string;
}

export interface IntegerMulZMZResponse {
  success: boolean;
  result: {
    sign: ZeroOrOne;
    digits: number[];
    string: string;
  };
  error?: string;
}

export interface NaturalTransNZResponse {
  success: boolean;
  result: {
    sign: ZeroOrOne;
    absolute: number[];
    string: string;
  };
  error?: string;
}

export interface IntegerTransZNResponse {
  success: boolean;
  result: Natural;
  error?: string;
}

export interface IntegerAddZZZRequest {
  a: Integer;
  b: Integer;
}

export interface IntegerAddZZZResponse {
  success: boolean;
  result: {
    absolute: number;
    sign: ZeroOrOne;
    string: string;
  };
  error?: string;
}

export interface IntegerSubZZZRequest {
  a: Integer;
  b: Integer;
}

export interface IntegerSubZZZResponse {
  success: boolean;
  result: {
    absolute: number;
    sign: ZeroOrOne;
    string: string;
  };
  error?: string;
}

export interface IntegerMulZZZRequest {
  a: Integer;
  b: Integer;
}

export interface IntegerMulZZZResponse {
  success: boolean;
  result: {
    absolute: number;
    sign: ZeroOrOne;
    string: string;
  };
  error?: string;
}

export interface IntegerDivZZZRequest {
  a: Integer;
  b: Integer;
}

export interface IntegerDivZZZResponse {
  success: boolean;
  result: {
    absolute: number;
    sign: ZeroOrOne;
    string: string;
  };
  error?: string;
}

export interface IntegerModZZZRequest {
  a: Integer;
  b: Integer;
}

export interface IntegerModZZZResponse {
  success: boolean;
  result: {
    absolute: number;
    sign: ZeroOrOne;
    string: string;
  };
  error?: string;
}

export interface RationalRedQQResponse {
  success: boolean;
  result: {
    numerator: Integer;
    denominator: Natural;
    string: string;
  };
  error?: string;
}

export interface RationalIntQBResponse {
  success: boolean;
  result: "да" | "нет";
  description: string;
  error?: string;
}

export interface RationalTransZQResponse {
  success: boolean;
  result: {
    numerator: Integer;
    denominator: Natural;
    string: string;
  };
  error?: string;
}

export interface RationalTransQZResponse {
  success: boolean;
  result: {
    sign: ZeroOrOne;
    absolute: number;
    string: string;
  };
  error?: string;
}

export interface RationalAddQQQRequest {
  a: Rational;
  b: Rational;
}

export interface RationalAddQQQResponse {
  success: boolean;
  result: {
    numerator: Integer;
    denominator: Natural;
    string: string;
  };
  error?: string;
}

export interface RationalSubQQQRequest {
  a: Rational;
  b: Rational;
}

export interface RationalSubQQQResponse {
  success: boolean;
  result: {
    numerator: Integer;
    denominator: Natural;
    string: string;
  };
  error?: string;
}

export interface RationalMulQQQRequest {
  a: Rational;
  b: Rational;
}

export interface RationalMulQQQResponse {
  success: boolean;
  result: {
    numerator: Integer;
    denominator: Natural;
    string: string;
  };
  error?: string;
}

export interface RationalDivQQQRequest {
  a: Rational;
  b: Rational;
}

export interface RationalDivQQQResponse {
  success: boolean;
  result: {
    numerator: Integer;
    denominator: Natural;
    string: string;
  };
  error?: string;
}

export interface PolynomialRequest {
  polynomial: Polynomial;
}

export interface TwoPolynomialsRequest {
  a: Polynomial;
  b: Polynomial;
}

export interface PolynomialAndRationalRequest {
  polynomial: Polynomial;
  rational: Rational;
}

export interface PolynomialAndNaturalRequest {
  polynomial: Polynomial;
  k: Natural;
}

export interface PolynomialResponse {
  success: boolean;
  result: PolynomialRepresentation;
  error?: string;
}

export interface PolynomialBooleanResponse {
  success: boolean;
  result: boolean;
  description: string;
  error?: string;
}

export interface PolynomialRationalResponse {
  success: boolean;
  result: Rational;
  error?: string;
}

export interface PolynomialNaturalResponse {
  success: boolean;
  result: Natural;
  error?: string;
}

export interface PolynomialAddPPRequest extends TwoPolynomialsRequest {}
export interface PolynomialAddPPResponse extends PolynomialResponse {}

export interface PolynomialSubPPRequest extends TwoPolynomialsRequest {}
export interface PolynomialSubPPResponse extends PolynomialResponse {}

export interface PolynomialMulPPRequest extends TwoPolynomialsRequest {}
export interface PolynomialMulPPResponse extends PolynomialResponse {}

export interface PolynomialDivPPRequest extends TwoPolynomialsRequest {}
export interface PolynomialDivPPResponse extends PolynomialResponse {}

export interface PolynomialModPPRequest extends TwoPolynomialsRequest {}
export interface PolynomialModPPResponse extends PolynomialResponse {}

export interface PolynomialMulPQRequest extends PolynomialAndRationalRequest {}
export interface PolynomialMulPQResponse extends PolynomialResponse {}

export interface PolynomialMulPxkRequest extends PolynomialAndNaturalRequest {}
export interface PolynomialMulPxkResponse extends PolynomialResponse {}

export interface PolynomialLedPQRequest extends PolynomialRequest {}
export interface PolynomialLedPQResponse extends PolynomialRationalResponse {}

export interface PolynomialDegPNRequest extends PolynomialRequest {}
export interface PolynomialDegPNResponse extends PolynomialNaturalResponse {}

export interface PolynomialFacPQRequest extends PolynomialRequest {}
export interface PolynomialFacPQResponse extends PolynomialRationalResponse {}

export interface PolynomialDerPPRequest extends PolynomialRequest {}
export interface PolynomialDerPPResponse extends PolynomialResponse {}

export interface PolynomialNmrPPRequest extends PolynomialRequest {}
export interface PolynomialNmrPPResponse extends PolynomialResponse {}

export interface PolynomialGcfPPRequest extends TwoPolynomialsRequest {}
export interface PolynomialGcfPPResponse extends PolynomialResponse {}

export interface PolynomialIsZeroRequest extends PolynomialRequest {}
export interface PolynomialIsZeroResponse extends PolynomialBooleanResponse {}
