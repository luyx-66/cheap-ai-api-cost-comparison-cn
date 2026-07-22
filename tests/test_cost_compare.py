import unittest

from cost_compare import estimate, validate


class CostTests(unittest.TestCase):
    def test_estimate(self):
        provider = {"name": "p", "currency": "USD", "source": "https://example.com", "checked_at": "2026-01-01", "input_per_million": 1, "output_per_million": 4, "image_unit_price": 0.05}
        row = estimate(provider, {"input_tokens": 1_000_000, "output_tokens": 500_000, "images": 2, "video_seconds": 0})
        self.assertEqual(row["total_cost"], 3.1)

    def test_required_source(self):
        with self.assertRaises(ValueError):
            validate([{"name": "p", "currency": "USD", "checked_at": "2026-01-01"}])

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            validate([{"name": "p", "currency": "USD", "source": "x", "checked_at": "d", "input_per_million": -1}])


if __name__ == "__main__":
    unittest.main()
