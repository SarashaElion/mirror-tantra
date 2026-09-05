import unittest

from mirror_tantra import MirrorMode, MirrorTantraEngine


class MirrorTantraSmokeTests(unittest.TestCase):
    def setUp(self):
        self.engine = MirrorTantraEngine("mirror_tantra.json")

    def test_protocols_load(self):
        self.assertGreater(len(self.engine.list_protocol_ids()), 0)

    def test_shadow_prompt_maps_transparently(self):
        mode = self.engine.resolve_mode_from_prompt("Show me the shadow in this pattern")
        self.assertEqual(mode, MirrorMode.SHADOW)

    def test_context_payload_is_machine_readable(self):
        mode, payload = self.engine.ritual_context_for_prompt("Mirror me")
        self.assertEqual(mode, MirrorMode.OPEN)
        self.assertIn("mode", payload)
        self.assertIn("notes", payload)


if __name__ == "__main__":
    unittest.main()
