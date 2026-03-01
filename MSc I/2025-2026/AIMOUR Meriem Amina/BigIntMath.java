package tp1crypto;
import java.math.BigInteger;

public class BigIntMath {

    public static class GCDResult {
        public BigInteger d;
        public BigInteger u;
        public BigInteger v;

        public GCDResult(BigInteger d, BigInteger u, BigInteger v) {
            this.d = d;
            this.u = u;
            this.v = v;
        }
    }

    public static GCDResult extendedGCD(BigInteger a, BigInteger b) {

        BigInteger r = a;
        BigInteger rPrime = b;

        BigInteger u = BigInteger.ONE;
        BigInteger v = BigInteger.ZERO;

        BigInteger uPrime = BigInteger.ZERO;
        BigInteger vPrime = BigInteger.ONE;

        while (!rPrime.equals(BigInteger.ZERO)) {

            BigInteger q = r.divide(rPrime);

            BigInteger tempR = rPrime;
            BigInteger tempU = uPrime;
            BigInteger tempV = vPrime;

            rPrime = r.subtract(q.multiply(rPrime));
            uPrime = u.subtract(q.multiply(uPrime));
            vPrime = v.subtract(q.multiply(vPrime));

            r = tempR;
            u = tempU;
            v = tempV;
        }

        return new GCDResult(r, u, v);
    }

    public static BigInteger modInverse(BigInteger a, BigInteger n) {

        GCDResult result = extendedGCD(a, n);

        if (!result.d.equals(BigInteger.ONE)) {
            throw new ArithmeticException("Inverse modulaire inexistant");
        }

        return result.u.mod(n);
    }
}