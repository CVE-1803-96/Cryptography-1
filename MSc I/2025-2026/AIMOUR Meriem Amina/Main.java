package tp1crypto;
import java.math.BigInteger;

public class Main {

    public static void main(String[] args) {

        BigInteger a = new BigInteger("5");
        BigInteger b = new BigInteger("8");
        BigInteger n = new BigInteger("26");

        AffineCipher cipher = new AffineCipher(a, b, n);

        BigInteger message = new BigInteger("7");

        BigInteger encrypted = cipher.encrypt(message);
        BigInteger decrypted = cipher.decrypt(encrypted);

        System.out.println("Message original : " + message);
        System.out.println("Message chiffré : " + encrypted);
        System.out.println("Message déchiffré : " + decrypted);
    }
}