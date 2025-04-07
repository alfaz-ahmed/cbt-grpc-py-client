# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from com.nutanix.dataprotection.v4.content import VMRecoveryPointComputeChangedRegions_service_pb2 as com_dot_nutanix_dot_dataprotection_dot_v4_dot_content_dot_VMRecoveryPointComputeChangedRegions__service__pb2

GRPC_GENERATED_VERSION = '1.70.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in com/nutanix/dataprotection/v4/content/VMRecoveryPointComputeChangedRegions_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class VMRecoveryPointComputeChangedRegionsServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.vmRecoveryPointComputeChangedRegions = channel.unary_stream(
                '/com.nutanix.dataprotection.v4.content.VMRecoveryPointComputeChangedRegionsService/vmRecoveryPointComputeChangedRegions',
                request_serializer=com_dot_nutanix_dot_dataprotection_dot_v4_dot_content_dot_VMRecoveryPointComputeChangedRegions__service__pb2.VmRecoveryPointComputeChangedRegionsArg.SerializeToString,
                response_deserializer=com_dot_nutanix_dot_dataprotection_dot_v4_dot_content_dot_VMRecoveryPointComputeChangedRegions__service__pb2.VmRecoveryPointComputeChangedRegionsRet.FromString,
                _registered_method=True)


class VMRecoveryPointComputeChangedRegionsServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def vmRecoveryPointComputeChangedRegions(self, request, context):
        """
        uri: /dataprotection/v4/content/recovery-points/{recoveryPointExtId}/vm-recovery-points/{vmRecoveryPointExtId}/disk-recovery-points/{extId}/$actions/compute-changed-regions
        http method: POST
        Changed Regions information for the regions that have changed in the right half-open interval
        Returns information pertaining to all the regions that have changed in the right half-open interval: [start, length).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_VMRecoveryPointComputeChangedRegionsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'vmRecoveryPointComputeChangedRegions': grpc.unary_stream_rpc_method_handler(
                    servicer.vmRecoveryPointComputeChangedRegions,
                    request_deserializer=com_dot_nutanix_dot_dataprotection_dot_v4_dot_content_dot_VMRecoveryPointComputeChangedRegions__service__pb2.VmRecoveryPointComputeChangedRegionsArg.FromString,
                    response_serializer=com_dot_nutanix_dot_dataprotection_dot_v4_dot_content_dot_VMRecoveryPointComputeChangedRegions__service__pb2.VmRecoveryPointComputeChangedRegionsRet.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.nutanix.dataprotection.v4.content.VMRecoveryPointComputeChangedRegionsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('com.nutanix.dataprotection.v4.content.VMRecoveryPointComputeChangedRegionsService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class VMRecoveryPointComputeChangedRegionsService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def vmRecoveryPointComputeChangedRegions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/com.nutanix.dataprotection.v4.content.VMRecoveryPointComputeChangedRegionsService/vmRecoveryPointComputeChangedRegions',
            com_dot_nutanix_dot_dataprotection_dot_v4_dot_content_dot_VMRecoveryPointComputeChangedRegions__service__pb2.VmRecoveryPointComputeChangedRegionsArg.SerializeToString,
            com_dot_nutanix_dot_dataprotection_dot_v4_dot_content_dot_VMRecoveryPointComputeChangedRegions__service__pb2.VmRecoveryPointComputeChangedRegionsRet.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
