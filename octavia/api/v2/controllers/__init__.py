#    Copyright 2016 Intel
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from wsme import types as wtypes
from wsmeext import pecan as wsme_pecan

from octavia.api.v2.controllers import base
from octavia.api.v2.controllers import listener
from octavia.api.v2.controllers import load_balancer


class BaseV2Controller(base.BaseController):
    loadbalancers = load_balancer.LoadBalancersController()
    listeners = listener.ListenersController()

    @wsme_pecan.wsexpose(wtypes.text)
    def get(self):
        return "v2.0"


class LBaaSController(BaseV2Controller):
    """Expose /lbaas/ endpoint for the v2.0 controller.

    Provides backwards compatibility with LBaaSV2

    To be removed once LBaasV2 has been removed.

    """
    pass


class V2Controller(BaseV2Controller):
    lbaas = LBaaSController()
