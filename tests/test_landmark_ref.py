# Copyright 2024 cvpose
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from custom_landmarks.landmark_ref import LandmarkRef


def test_landmark_ref_behaves_like_tuple():
    ref = LandmarkRef(lambda: (0.1, 0.2, 0.3), lambda: 42)

    assert ref.value == 42
    assert list(ref) == [0.1, 0.2, 0.3]
    assert ref[1] == 0.2
    assert repr(ref) == repr((0.1, 0.2, 0.3))