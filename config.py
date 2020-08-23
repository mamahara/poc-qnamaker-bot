#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    QNA_KNOWLEDGEBASE_ID = os.environ.get("QnAKnowledgebaseId", "db410632-3b57-4410-a28d-64fe367b11cb")
    QNA_ENDPOINT_KEY = os.environ.get("QnAEndpointKey", "3347cbe7-b29a-4488-a879-9937917c70ca")
    QNA_ENDPOINT_HOST = os.environ.get("QnAEndpointHostName", "https://poc-qna-knowledgebase-svc.azurewebsites.net/qnamaker")


