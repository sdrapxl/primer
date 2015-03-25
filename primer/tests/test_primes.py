#! /usr/bin/env python

"""Tests for the primer package."""

import unittest
import primer

primes_10 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, ]
primes_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
              53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
              109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167,
              173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
              233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283,
              293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359,
              367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431,
              433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491,
              499, 503, 509, 521, 523, 541, ]
primorial_10 = 6469693230
primorial_100 = long("471193079990618495316248783476026042202057477340"
                     "967552018863483961641533584503422120528925670554"
                     "468197243910409777715799180438028421831503871944"
                     "494399049257903072063599053845231252833986435299"
                     "9310398481791730017201031090L")


class TestPGF(unittest.TestCase):
    """TestCase for primer.pgf."""

    def test_generator(self):
        """Does calling pgf return a generator?"""
        pg = primer.pgf()
        self.assertTrue(hasattr(pg, 'next'))


class TestPrimes(unittest.TestCase):
    """TestCase for primer.primes."""

    def test_primes_10(self):
        """"Compute the first 10 primes."""

        self.assertEqual(primer.primes(10), primes_10)

    def test_primes_100(self):
        """Compute the first 100 primes."""

        self.assertEqual(primer.primes(100), primes_100)

    def test_primes_str(self):
        """Does calling primes with a string argument raise a TypeError?"""

        with self.assertRaises(TypeError):
            primer.primes("100")

    def test_primes_float(self):
        """Does calling primes with a float argument raise a TypeError?"""

        with self.assertRaises(TypeError):
            primer.primes(10.0)


class TestPrime(unittest.TestCase):
    """TestCase for primer.prime."""

    def test_prime_10(self):
        """Compute the 10th prime."""

        self.assertEqual(primer.prime(10), primes_10[-1])

    def test_prime_100(self):
        """Compute the 100th prime."""
        self.assertEqual(primer.prime(100), primes_100[-1])

    def test_prime_str(self):
        """Does calling prime with a string argument raise a TypeError?"""

        with self.assertRaises(TypeError):
            primer.prime("100")

    def test_prime_float(self):
        """Does calling prime with a float argument raise a TypeError?"""

        with self.assertRaises(TypeError):
            primer.prime(10.0)

    def test_prime_zero(self):
        """Does calling prime with 0 raise an IndexError?"""

        with self.assertRaises(IndexError):
            primer.prime(0)

    def test_prime_negative(self):
        """Does calling prime with a negative int raise an IndexError?"""

        with self.assertRaises(IndexError):
            primer.prime(-10)


class TestPrimorial(unittest.TestCase):
    """TestCase for primer.primorial."""

    def test_primorial_10(self):
        """Compute the 10th primorial."""

        self.assertEqual(primer.primorial(10), primorial_10)

    def test_primorial_100(self):
        """Compute the 100th primorial."""

        self.assertEqual(primer.primorial(100), primorial_100)

    def test_primorial_str(self):
        """Does calling primorial with a string argument raise a TypeError?"""

        with self.assertRaises(TypeError):
            primer.primorial("100")

    def test_primorial_float(self):
        """Does calling primorial with a float argument raise a TypeError?"""

        with self.assertRaises(TypeError):
            primer.primorial(10.0)

    def test_primorial_zero(self):
        """Does calling primorial with 0 raise a TypeError?"""

        with self.assertRaises(TypeError):
            primer.primorial(0)

    def test_primorial_negative(self):
        """Does calling primorial with a negative int raise a TypeError?"""

        with self.assertRaises(TypeError):
            primer.primorial(-10)


if __name__ == "__main__":
    unittest.main()
