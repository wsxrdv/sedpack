# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# automatically generated by the FlatBuffers compiler, do not modify

# namespace: shardfile

# pylint: skip-file

import flatbuffers  # type: ignore
from flatbuffers.compat import import_numpy  # type: ignore

np = import_numpy()


class Attribute(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Attribute()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsAttribute(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)

    # Attribute
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Attribute
    def AttributeBytes(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(
                flatbuffers.number_types.Uint8Flags,
                a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Attribute
    def AttributeBytesAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(
                flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Attribute
    def AttributeBytesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Attribute
    def AttributeBytesIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0


def AttributeStart(builder):
    builder.StartObject(1)


def Start(builder):
    AttributeStart(builder)


def AttributeAddAttributeBytes(builder, attributeBytes):
    builder.PrependUOffsetTRelativeSlot(
        0, flatbuffers.number_types.UOffsetTFlags.py_type(attributeBytes), 0)


def AddAttributeBytes(builder, attributeBytes):
    AttributeAddAttributeBytes(builder, attributeBytes)


def AttributeStartAttributeBytesVector(builder, numElems):
    return builder.StartVector(1, numElems, 1)


def StartAttributeBytesVector(builder, numElems):
    return AttributeStartAttributeBytesVector(builder, numElems)


def AttributeEnd(builder):
    return builder.EndObject()


def End(builder):
    return AttributeEnd(builder)
