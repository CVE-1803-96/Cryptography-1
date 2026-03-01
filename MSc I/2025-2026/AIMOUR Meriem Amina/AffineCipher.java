package tp1crypto;
import java.math.BigInteger;

public class AffineCipher {

    private BigInteger a;
    private BigInteger b;
    private BigInteger n;

    public AffineCipher(BigInteger a, BigInteger b, BigInteger n) {

        if (!BigIntMath.extendedGCD(a, n).d.equals(BigInteger.ONE)) {
            throw new IllegalArgumentException("a et n ne sont pas premiers entre eux");
        }

        this.a = a;
        this.b = b;
        this.n = n;
    }

    public BigInteger encrypt(BigInteger m) {
        return (a.multiply(m).add(b)).mod(n);
    }

    public BigInteger decrypt(BigInteger c) {

        BigInteger aInv = BigIntMath.modInverse(a, n);

        return aInv.multiply(c.subtract(b)).mod(n);
    }
}