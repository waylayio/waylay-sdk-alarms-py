import json
import yaml


def with_example_provider(dct):
    has_example = False
    if "example" in dct:
        example, has_example = dct["example"], True
    elif "examples" in dct:
        examples = dct["examples"]
        if isinstance(examples, list) and list:
            example, has_example = examples[0], True
    elif "default" in dct:
        example, has_example = dct["default"], True

    if has_example:
        provider = (
            example
            if example is None or isinstance(example, (dict, list, int, float, bool))
            else f"'{example}'"
        )
        dct.update({"$provider": f"lambda: {provider}"})
    return dct


with open("openapi/alarms.transformed.openapi.yaml", "r") as file:
    OPENAPI_SPEC = yaml.safe_load(file)

MODEL_DEFINITIONS = OPENAPI_SPEC["components"]["schemas"]

_a_batch_alarms_specification_model_schema = json.loads(
    r"""{
  "title" : "a batch alarms specification",
  "type" : "object",
  "oneOf" : [ {
    "$ref" : "#/components/schemas/BatchUpdateAlarm"
  }, {
    "$ref" : "#/components/schemas/BatchDeleteAlarm"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update(
    {"a_batch_alarms_specification": _a_batch_alarms_specification_model_schema}
)

_alarm_audit_record_model_schema = json.loads(
    r"""{
  "title" : "AlarmAuditRecord",
  "required" : [ "id", "text", "timestamp", "type" ],
  "type" : "object",
  "properties" : {
    "id" : {
      "title" : "id",
      "type" : "string",
      "example" : "ca0c5181-11dc-47dd-aeb3-a7a508ea1599\""
    },
    "type" : {
      "$ref" : "#/components/schemas/AlarmEventType"
    },
    "text" : {
      "title" : "text",
      "type" : "string",
      "description" : "Text describing the change",
      "example" : "Alarm raised"
    },
    "timestamp" : {
      "title" : "timestamp",
      "allOf" : [ {
        "$ref" : "#/components/schemas/SO8601Timestamp"
      }, {
        "description" : "timestamp when the change happened"
      } ]
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"AlarmAuditRecord": _alarm_audit_record_model_schema})

_alarm_entity_model_schema = json.loads(
    r"""{
  "required" : [ "count", "creationTime", "id", "lastTriggeredTime", "lastUpdateTime", "severity", "source", "status", "text", "timestamp", "type" ],
  "type" : "object",
  "properties" : {
    "id" : {
      "$ref" : "#/components/schemas/AlarmId"
    },
    "creationTime" : {
      "$ref" : "#/components/schemas/SO8601Timestamp"
    },
    "lastUpdateTime" : {
      "$ref" : "#/components/schemas/SO8601Timestamp"
    },
    "lastTriggeredTime" : {
      "$ref" : "#/components/schemas/SO8601Timestamp"
    },
    "type" : {
      "$ref" : "#/components/schemas/AlarmType"
    },
    "text" : {
      "$ref" : "#/components/schemas/AlarmText"
    },
    "timestamp" : {
      "$ref" : "#/components/schemas/SO8601Timestamp"
    },
    "source" : {
      "$ref" : "#/components/schemas/IdObject"
    },
    "severity" : {
      "$ref" : "#/components/schemas/AlarmSeverity"
    },
    "status" : {
      "$ref" : "#/components/schemas/AlarmStatus"
    },
    "count" : {
      "title" : "Event count",
      "minimum" : 1,
      "type" : "integer",
      "description" : "The number of times this alarm has been sent"
    },
    "assignee" : {
      "$ref" : "#/components/schemas/AlarmAssignee"
    },
    "history" : {
      "title" : "History of modifications",
      "minItems" : 1,
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/AlarmAuditRecord"
      }
    },
    "self" : {
      "$ref" : "#/components/schemas/AlarmSelfLink"
    },
    "additionalProperties" : {
      "type" : "object",
      "description" : "Additional properties that were present in the creation payload",
      "example" : {
        "task" : "1e294c8b-8a7d-4770-997e-2d57fc5ad6ea",
        "myRef" : "902d4191-d1ab-47ae-8405-c33bb237f1d5"
      }
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"AlarmEntity": _alarm_entity_model_schema})

_alarm_event_model_schema = json.loads(
    r"""{
  "required" : [ "alarm", "eventtime", "eventtype" ],
  "type" : "object",
  "properties" : {
    "eventtype" : {
      "$ref" : "#/components/schemas/AlarmEventType"
    },
    "eventtime" : {
      "$ref" : "#/components/schemas/SO8601Timestamp"
    },
    "alarm" : {
      "$ref" : "#/components/schemas/AlarmEventAlarm"
    },
    "changes" : {
      "type" : "array",
      "description" : "Describes the changes that where done\n\nWill only be there if `eventtype` is `io.waylay.alarm.AlarmUpdated`",
      "items" : {
        "$ref" : "#/components/schemas/AlarmEvent_changes_inner"
      }
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"AlarmEvent": _alarm_event_model_schema})

_alarm_event_alarm_model_schema = json.loads(
    r"""{
  "title" : "AlarmEventAlarm",
  "required" : [ "count", "creationTime", "id", "severity", "source", "status", "tenantId", "text", "timestamp", "type" ],
  "type" : "object",
  "properties" : {
    "id" : {
      "$ref" : "#/components/schemas/AlarmId"
    },
    "tenantId" : {
      "title" : "tenantId",
      "type" : "string"
    },
    "creationTime" : {
      "$ref" : "#/components/schemas/SO8601Timestamp"
    },
    "type" : {
      "$ref" : "#/components/schemas/AlarmType"
    },
    "text" : {
      "$ref" : "#/components/schemas/AlarmText"
    },
    "timestamp" : {
      "$ref" : "#/components/schemas/SO8601Timestamp"
    },
    "source" : {
      "$ref" : "#/components/schemas/IdObject"
    },
    "severity" : {
      "$ref" : "#/components/schemas/AlarmSeverity"
    },
    "status" : {
      "$ref" : "#/components/schemas/AlarmStatus"
    },
    "count" : {
      "title" : "count",
      "minimum" : 1,
      "type" : "integer"
    }
  },
  "description" : "Summary representation of an alarm."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"AlarmEventAlarm": _alarm_event_alarm_model_schema})

_alarm_event_changes_inner_model_schema = json.loads(
    r"""{
  "title" : "AlarmEvent_changes_inner",
  "type" : "object",
  "properties" : {
    "attribute" : {
      "title" : "attribute",
      "type" : "string",
      "example" : "severity"
    },
    "type" : {
      "title" : "type",
      "type" : "string",
      "description" : "Indication of what has changed",
      "enum" : [ "io.waylay.alarm.change.severity", "io.waylay.alarm.change.status", "io.waylay.alarm.change.attribute" ]
    },
    "oldValue" : {
      "title" : "oldValue",
      "type" : "string",
      "nullable" : true,
      "example" : "MAJOR"
    },
    "newValue" : {
      "title" : "newValue",
      "type" : "string",
      "nullable" : true,
      "example" : "CRITICAL"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update(
    {"AlarmEvent_changes_inner": _alarm_event_changes_inner_model_schema}
)

_alarm_event_type_model_schema = json.loads(
    r"""{
  "title" : "AlarmEventType",
  "type" : "string",
  "oneOf" : [ {
    "title" : "Alarm Creation Event Type",
    "type" : "string",
    "description" : "A new alarm was created.",
    "enum" : [ "io.waylay.alarm.AlarmRaised" ]
  }, {
    "title" : "Alarm Event Happened Again Event type",
    "type" : "string",
    "description" : "An alarm happened again.",
    "enum" : [ "io.waylay.alarm.EventOccuredAgain" ]
  }, {
    "title" : "Alarm Update Event Type",
    "type" : "string",
    "description" : "An alarm was updated.",
    "enum" : [ "io.waylay.alarm.AlarmUpdated" ]
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"AlarmEventType": _alarm_event_type_model_schema})

_alarm_severity_model_schema = json.loads(
    r"""{
  "title" : "AlarmSeverity",
  "type" : "string",
  "enum" : [ "CRITICAL", "MAJOR", "MINOR", "WARNING" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"AlarmSeverity": _alarm_severity_model_schema})

_alarm_severity_filter_model_schema = json.loads(
    r"""{
  "title" : "Alarm Severity Filter",
  "oneOf" : [ {
    "$ref" : "#/components/schemas/AlarmSeverity"
  }, {
    "type" : "array",
    "items" : {
      "$ref" : "#/components/schemas/AlarmSeverity"
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Alarm_Severity_Filter": _alarm_severity_filter_model_schema})

_alarm_source_filter_model_schema = json.loads(
    r"""{
  "title" : "Alarm Source Filter",
  "oneOf" : [ {
    "type" : "string"
  }, {
    "type" : "array",
    "items" : {
      "type" : "string"
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Alarm_Source_Filter": _alarm_source_filter_model_schema})

_alarm_status_model_schema = json.loads(
    r"""{
  "title" : "AlarmStatus",
  "type" : "string",
  "default" : "ACTIVE",
  "enum" : [ "ACTIVE", "ACKNOWLEDGED", "CLEARED" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"AlarmStatus": _alarm_status_model_schema})

_alarm_status_filter_model_schema = json.loads(
    r"""{
  "title" : "Alarm Status Filter",
  "oneOf" : [ {
    "$ref" : "#/components/schemas/AlarmStatus"
  }, {
    "type" : "array",
    "items" : {
      "$ref" : "#/components/schemas/AlarmStatus"
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Alarm_Status_Filter": _alarm_status_filter_model_schema})

_alarm_timeline_info_model_schema = json.loads(
    r"""{
  "required" : [ "creationTime", "id", "severity", "source", "status", "text", "timestamp", "type" ],
  "type" : "object",
  "properties" : {
    "id" : {
      "$ref" : "#/components/schemas/AlarmId"
    },
    "creationTime" : {
      "$ref" : "#/components/schemas/SO8601Timestamp"
    },
    "timestamp" : {
      "$ref" : "#/components/schemas/SO8601Timestamp"
    },
    "source" : {
      "$ref" : "#/components/schemas/IdObject"
    },
    "type" : {
      "$ref" : "#/components/schemas/AlarmType"
    },
    "text" : {
      "$ref" : "#/components/schemas/AlarmText"
    },
    "severity" : {
      "$ref" : "#/components/schemas/AlarmSeverity"
    },
    "status" : {
      "$ref" : "#/components/schemas/AlarmStatus"
    },
    "assignee" : {
      "$ref" : "#/components/schemas/AlarmAssignee"
    }
  },
  "description" : "The alarm as it is after the event"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"AlarmTimelineInfo": _alarm_timeline_info_model_schema})

_alarm_type_filter_model_schema = json.loads(
    r"""{
  "title" : "Alarm Type Filter",
  "oneOf" : [ {
    "$ref" : "#/components/schemas/AlarmType"
  }, {
    "type" : "array",
    "items" : {
      "$ref" : "#/components/schemas/AlarmType"
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Alarm_Type_Filter": _alarm_type_filter_model_schema})

_alarm_update_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "severity" : {
      "$ref" : "#/components/schemas/AlarmSeverity"
    },
    "status" : {
      "$ref" : "#/components/schemas/AlarmStatus"
    },
    "assignee" : {
      "allOf" : [ {
        "$ref" : "#/components/schemas/AlarmAssignee"
      }, {
        "nullable" : true
      } ]
    }
  },
  "description" : "At least one field must be specified."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"AlarmUpdate": _alarm_update_model_schema})

_alarms_query_result_model_schema = json.loads(
    r"""{
  "required" : [ "alarms", "self", "total" ],
  "type" : "object",
  "properties" : {
    "self" : {
      "type" : "string",
      "description" : "Link to alarm query",
      "format" : "uri",
      "example" : "/alarms/v1/alarms?page=3"
    },
    "alarms" : {
      "title" : "List of alarms",
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/AlarmEntity"
      }
    },
    "total" : {
      "type" : "integer",
      "description" : "Total number of alarms that fulfill the criteria",
      "example" : 248
    },
    "next" : {
      "type" : "string",
      "description" : "Link to the next page of results (if more results are available)",
      "format" : "uri",
      "example" : "/alarms/v1/alarms?page=4"
    },
    "prev" : {
      "type" : "string",
      "description" : "Link to the previous page of result (if previous page is available)",
      "format" : "uri",
      "example" : "/alarms/v1/alarms?page=2"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"AlarmsQueryResult": _alarms_query_result_model_schema})

_alarms_timeline_item_model_schema = json.loads(
    r"""{
  "required" : [ "alarm", "timestamp", "type" ],
  "type" : "object",
  "properties" : {
    "timestamp" : {
      "$ref" : "#/components/schemas/AlarmTimelineTimestamp"
    },
    "type" : {
      "$ref" : "#/components/schemas/AlarmEventType"
    },
    "alarm" : {
      "$ref" : "#/components/schemas/AlarmTimelineInfo"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"AlarmsTimelineItem": _alarms_timeline_item_model_schema})

_batch_alarm_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "entity" : {
      "$ref" : "#/components/schemas/BatchAlarmEntity"
    },
    "action" : {
      "type" : "string"
    },
    "query" : {
      "type" : "object"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"BatchAlarm": _batch_alarm_model_schema})

_batch_alarm_entity_model_schema = json.loads(
    r"""{
  "type" : "string",
  "enum" : [ "alarm" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"BatchAlarmEntity": _batch_alarm_entity_model_schema})

_batch_delete_alarm_model_schema = json.loads(
    r"""{
  "required" : [ "action", "entity", "query" ],
  "type" : "object",
  "allOf" : [ {
    "$ref" : "#/components/schemas/BatchAlarm"
  }, {
    "properties" : {
      "action" : {
        "type" : "string",
        "enum" : [ "delete" ]
      },
      "query" : {
        "$ref" : "#/components/schemas/BatchDeleteAlarm_allOf_query"
      }
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"BatchDeleteAlarm": _batch_delete_alarm_model_schema})

_batch_delete_alarm_all_of_query_model_schema = json.loads(
    r"""{
  "title" : "BatchDeleteAlarm_allOf_query",
  "oneOf" : [ {
    "$ref" : "#/components/schemas/BulkQueryIds"
  }, {
    "$ref" : "#/components/schemas/BulkQueryFilter"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update(
    {"BatchDeleteAlarm_allOf_query": _batch_delete_alarm_all_of_query_model_schema}
)

_batch_operation_model_schema = json.loads(
    r"""{
  "required" : [ "id", "operation", "queueTime", "user" ],
  "type" : "object",
  "properties" : {
    "id" : {
      "$ref" : "#/components/schemas/BatchId"
    },
    "user" : {
      "type" : "string",
      "description" : "User id of the user who started the operation",
      "example" : "user/22f6dfdf-a50c-4eab-953e-8d2e56891dbe"
    },
    "operation" : {
      "$ref" : "#/components/schemas/BatchOperation_operation"
    },
    "queueTime" : {
      "$ref" : "#/components/schemas/SO8601Timestamp"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"BatchOperation": _batch_operation_model_schema})

_batch_operation_enqueued_model_schema = json.loads(
    r"""{
  "title" : "Batch operation enqueued",
  "required" : [ "entity", "statusCode", "uri" ],
  "type" : "object",
  "properties" : {
    "statusCode" : {
      "type" : "integer",
      "example" : 202
    },
    "uri" : {
      "type" : "string",
      "description" : "URI where the batch operation status can be followed",
      "format" : "uri",
      "example" : "/alarms/v1/batch/afcea5a1-81df-44f6-bd34-e0b602a2cf3d"
    },
    "entity" : {
      "$ref" : "#/components/schemas/Batch_operation_enqueued_entity"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update(
    {"Batch_operation_enqueued": _batch_operation_enqueued_model_schema}
)

_batch_operation_enqueued_entity_model_schema = json.loads(
    r"""{
  "required" : [ "id", "operation", "queueTime" ],
  "type" : "object",
  "properties" : {
    "id" : {
      "$ref" : "#/components/schemas/BatchId"
    },
    "queueTime" : {
      "$ref" : "#/components/schemas/SO8601Timestamp"
    },
    "operation" : {
      "$ref" : "#/components/schemas/Queued_operation_summary"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update(
    {"Batch_operation_enqueued_entity": _batch_operation_enqueued_entity_model_schema}
)

_batch_operation_operation_model_schema = json.loads(
    r"""{
  "title" : "BatchOperation_operation",
  "required" : [ "action", "description", "entity" ],
  "type" : "object",
  "properties" : {
    "entity" : {
      "$ref" : "#/components/schemas/BatchAlarmEntity"
    },
    "action" : {
      "title" : "action",
      "type" : "string",
      "enum" : [ "delete", "update" ]
    },
    "description" : {
      "title" : "description",
      "type" : "string",
      "description" : "Description of the operation",
      "example" : "deleting 3 alarms"
    }
  },
  "description" : "Summary of the batch operation"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update(
    {"BatchOperation_operation": _batch_operation_operation_model_schema}
)

_batch_operation_result_model_schema = json.loads(
    r"""{
  "example" : {
    "id" : "afcea5a1-81df-44f6-bd34-e0b602a2cf3d",
    "user" : "user/22f6dfdf-a50c-4eab-953e-8d2e56891dbe",
    "operation" : {
      "entity" : "alarm",
      "action" : "delete",
      "description" : "deleting 3 alarms"
    },
    "queueTime" : "2020-04-27T09:54:44.051Z",
    "finishedTime" : "2020-04-27T09:54:44.129Z",
    "results" : {
      "success" : {
        "df036bf8-4b32-4bd8-8ee7-42800ab26bf5" : {
          "statusCode" : 204
        }
      },
      "failure" : {
        "586ac2f2-fbec-426a-b696-d63d6cb153ac" : {
          "statusCode" : "404,",
          "error" : "alarm with id '586ac2f2-fbec-426a-b696-d63d6cb153ac' not found"
        },
        "e64de65c-e3ef-482d-9eb7-32ca17d1e147" : {
          "statusCode" : "404,",
          "error" : "alarm with id 'e64de65c-e3ef-482d-9eb7-32ca17d1e147' not found"
        }
      }
    }
  },
  "allOf" : [ {
    "$ref" : "#/components/schemas/BatchOperation"
  }, {
    "$ref" : "#/components/schemas/OperationResultObject"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"BatchOperationResult": _batch_operation_result_model_schema})

_batch_operation_results_model_schema = json.loads(
    r"""{
  "title" : "BatchOperationResults",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/BatchOperationResult"
  }, {
    "$ref" : "#/components/schemas/BatchOperation"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update(
    {"BatchOperationResults": _batch_operation_results_model_schema}
)

_batch_update_alarm_model_schema = json.loads(
    r"""{
  "required" : [ "action", "actionParameters", "entity", "query" ],
  "type" : "object",
  "allOf" : [ {
    "$ref" : "#/components/schemas/BatchAlarm"
  }, {
    "properties" : {
      "actionParameters" : {
        "$ref" : "#/components/schemas/AlarmUpdate"
      },
      "action" : {
        "type" : "string",
        "enum" : [ "update" ]
      },
      "query" : {
        "$ref" : "#/components/schemas/BulkQueryIds"
      }
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"BatchUpdateAlarm": _batch_update_alarm_model_schema})

_bulk_query_filter_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "type" : {
      "$ref" : "#/components/schemas/Alarm_Type_Filter"
    },
    "status" : {
      "$ref" : "#/components/schemas/Alarm_Status_Filter"
    },
    "severity" : {
      "$ref" : "#/components/schemas/Alarm_Severity_Filter"
    },
    "source" : {
      "$ref" : "#/components/schemas/Alarm_Source_Filter"
    },
    "dateFrom" : {
      "allOf" : [ {
        "$ref" : "#/components/schemas/UnixEpochMillis"
      }, {
        "title" : "Alarm timestamp filter (>=)"
      } ]
    },
    "dateTo" : {
      "allOf" : [ {
        "$ref" : "#/components/schemas/UnixEpochMillis"
      }, {
        "title" : "Alarm timestamp filter (<=)"
      } ]
    },
    "assignee" : {
      "$ref" : "#/components/schemas/AlarmAssignee"
    },
    "creationTimeFrom" : {
      "allOf" : [ {
        "$ref" : "#/components/schemas/UnixEpochMillis"
      }, {
        "title" : "Alarm creationTime filter (>=)"
      } ]
    },
    "creationTimeTo" : {
      "allOf" : [ {
        "$ref" : "#/components/schemas/UnixEpochMillis"
      }, {
        "title" : "Alarm creationTime filter (<=)"
      } ]
    },
    "lastUpdatedFrom" : {
      "allOf" : [ {
        "$ref" : "#/components/schemas/UnixEpochMillis"
      }, {
        "title" : "Alarm lastUpdateTime filter (>=)"
      } ]
    },
    "lastUpdatedTo" : {
      "allOf" : [ {
        "$ref" : "#/components/schemas/UnixEpochMillis"
      }, {
        "title" : "Alarm lastUpdateTime filter (<=)"
      } ]
    },
    "lastTriggeredFrom" : {
      "allOf" : [ {
        "$ref" : "#/components/schemas/UnixEpochMillis"
      }, {
        "title" : "Alarm lastTriggeredTime filter (>=)"
      } ]
    },
    "lastTriggeredTo" : {
      "allOf" : [ {
        "$ref" : "#/components/schemas/UnixEpochMillis"
      }, {
        "title" : "Alarm lastTriggeredTime filter (<=)"
      } ]
    }
  },
  "description" : "Object specifying filters on the alarm to which the operation will be applied.\nAt least one of the filters must be set."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"BulkQueryFilter": _bulk_query_filter_model_schema})

_bulk_query_ids_model_schema = json.loads(
    r"""{
  "title" : "BulkQueryIds",
  "required" : [ "ids" ],
  "type" : "object",
  "properties" : {
    "ids" : {
      "title" : "ids",
      "minItems" : 1,
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/AlarmId"
      }
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"BulkQueryIds": _bulk_query_ids_model_schema})

_cloud_alarm_event_model_schema = json.loads(
    r"""{
  "example" : {
    "time" : "2011-09-06T12:03:27.845Z",
    "type" : "io.waylay.alarms.v1.AlarmUpdated",
    "subject" : "289dd1a3-35a7-44fa-8596-9aee3ad0b36f/2c49e3bf-547b-42bc-a5e9-9193155ec03d"
  },
  "allOf" : [ {
    "$ref" : "./cloudevents.schema.yaml#/definitions/cloudevent_json"
  }, {
    "$ref" : "#/components/schemas/CloudAlarmEventData"
  }, {
    "required" : [ "subject", "time" ]
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"CloudAlarmEvent": _cloud_alarm_event_model_schema})

_cloud_alarm_event_data_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "id" : {
      "example" : "dd59d2d9-9657-4d36-b045-ef97315f2d20"
    },
    "source" : {
      "example" : "/alarms/v1/alarms"
    },
    "subject" : {
      "type" : "string",
      "example" : "289dd1a3-35a7-44fa-8596-9aee3ad0b36f/2c49e3bf-547b-42bc-a5e9-9193155ec03d"
    },
    "type" : {
      "type" : "string",
      "enum" : [ "io.waylay.alarms.v1.AlarmRaised", "io.waylay.alarms.v1.EventOccurredAgain", "io.waylay.alarms.v1.AlarmUpdated" ]
    },
    "data" : {
      "$ref" : "#/components/schemas/AlarmEvent"
    },
    "time" : {
      "$ref" : "#/components/schemas/SO8601Timestamp"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"CloudAlarmEventData": _cloud_alarm_event_data_model_schema})

_create_alarm_model_schema = json.loads(
    r"""{
  "required" : [ "severity", "source", "text", "type" ],
  "type" : "object",
  "properties" : {
    "type" : {
      "$ref" : "#/components/schemas/AlarmType"
    },
    "text" : {
      "$ref" : "#/components/schemas/AlarmText"
    },
    "severity" : {
      "$ref" : "#/components/schemas/AlarmSeverity"
    },
    "source" : {
      "$ref" : "#/components/schemas/IdObject"
    },
    "status" : {
      "$ref" : "#/components/schemas/AlarmStatus"
    },
    "timestamp" : {
      "$ref" : "#/components/schemas/SO8601TimestampOrMillis"
    },
    "assignee" : {
      "$ref" : "#/components/schemas/AlarmAssignee"
    }
  },
  "additionalProperties" : {
    "title" : "Additional properties",
    "description" : "Any additional properties provided upon creation will be stored in the `additionalProperties` field\nof the created alarm."
  },
  "description" : "To create an alarm, you need to provide the following mandatory inputs.",
  "example" : {
    "type" : "io.waylay.alarm.test",
    "text" : "Valve test failed",
    "severity" : "CRITICAL",
    "source" : {
      "id" : "733c06ed-7919-416a-9d19-8996821be70d"
    },
    "task" : "1e294c8b-8a7d-4770-997e-2d57fc5ad6ea",
    "myRef" : "902d4191-d1ab-47ae-8405-c33bb237f1d5"
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"CreateAlarm": _create_alarm_model_schema})

_error_response_model_schema = json.loads(
    r"""{
  "required" : [ "error", "statusCode" ],
  "type" : "object",
  "properties" : {
    "statusCode" : {
      "title" : "The error code",
      "type" : "integer",
      "example" : 400
    },
    "error" : {
      "title" : "The error message",
      "type" : "string",
      "example" : "error in body"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ErrorResponse": _error_response_model_schema})

_error_response_with_details_model_schema = json.loads(
    r"""{
  "allOf" : [ {
    "$ref" : "#/components/schemas/ErrorResponse"
  }, {
    "type" : "object",
    "properties" : {
      "details" : {
        "minItems" : 1,
        "type" : "array",
        "items" : {
          "type" : "string",
          "description" : "specific error message",
          "example" : "/severity <- Could not parse severity, valid values are: CRITICAL, MAJOR, MINOR, WARNING"
        }
      }
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update(
    {"ErrorResponseWithDetails": _error_response_with_details_model_schema}
)

_failure_operation_result_value_model_schema = json.loads(
    r"""{
  "title" : "FailureOperationResult_value",
  "required" : [ "error", "statusCode" ],
  "type" : "object",
  "properties" : {
    "statusCode" : {
      "title" : "statusCode",
      "type" : "integer",
      "description" : "The statusCode of the operation"
    },
    "error" : {
      "title" : "error",
      "type" : "string",
      "description" : "Error description of what went wrong."
    }
  },
  "description" : "The keys will be alarm ids."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update(
    {"FailureOperationResult_value": _failure_operation_result_value_model_schema}
)

_id_object_model_schema = json.loads(
    r"""{
  "title" : "IdObject",
  "required" : [ "id" ],
  "type" : "object",
  "properties" : {
    "id" : {
      "title" : "Resource Id",
      "type" : "string"
    }
  },
  "description" : "A JSON object with an id field indicating the resource.",
  "example" : {
    "id" : "12345"
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"IdObject": _id_object_model_schema})

_list_additional_query_params_parameter_value_model_schema = json.loads(
    r"""{
  "anyOf" : [ {
    "type" : "number"
  }, {
    "type" : "string"
  }, {
    "type" : "boolean"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update(
    {
        "list_additionalQueryParams_parameter_value": _list_additional_query_params_parameter_value_model_schema
    }
)

_nd_json_response_stream_model_schema = json.loads(
    r"""{
  "title" : "NdJsonResponseStream",
  "oneOf" : [ {
    "$ref" : "#/components/schemas/AlarmEvent"
  }, {
    "$ref" : "#/components/schemas/CloudAlarmEvent"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update(
    {"NdJsonResponseStream": _nd_json_response_stream_model_schema}
)

_operation_result_object_model_schema = json.loads(
    r"""{
  "required" : [ "finishedTime", "results" ],
  "type" : "object",
  "properties" : {
    "finishedTime" : {
      "$ref" : "#/components/schemas/SO8601Timestamp"
    },
    "results" : {
      "$ref" : "#/components/schemas/OperationResultObject_results"
    }
  },
  "description" : "Finished Batch Operation results"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update(
    {"OperationResultObject": _operation_result_object_model_schema}
)

_operation_result_object_results_model_schema = json.loads(
    r"""{
  "title" : "OperationResultObject_results",
  "required" : [ "failure", "success" ],
  "type" : "object",
  "properties" : {
    "success" : {
      "$ref" : "#/components/schemas/SuccessOperationResult"
    },
    "failure" : {
      "$ref" : "#/components/schemas/FailureOperationResult"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update(
    {"OperationResultObject_results": _operation_result_object_results_model_schema}
)

_queued_operation_summary_model_schema = json.loads(
    r"""{
  "title" : "Queued operation summary",
  "required" : [ "action", "entity" ],
  "type" : "object",
  "properties" : {
    "entity" : {
      "$ref" : "#/components/schemas/BatchAlarmEntity"
    },
    "action" : {
      "type" : "string",
      "enum" : [ "update", "delete" ]
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update(
    {"Queued_operation_summary": _queued_operation_summary_model_schema}
)

_so8601_timestamp_or_millis_model_schema = json.loads(
    r"""{
  "title" : "SO8601TimestampOrMillis",
  "description" : "ISO8601 timestamp or unix epoch milliseconds.",
  "oneOf" : [ {
    "$ref" : "#/components/schemas/UnixEpochMillis"
  }, {
    "$ref" : "#/components/schemas/SO8601Timestamp"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update(
    {"SO8601TimestampOrMillis": _so8601_timestamp_or_millis_model_schema}
)

_ss_event_stream_model_schema = json.loads(
    r"""{
  "title" : "SSEventStream",
  "oneOf" : [ {
    "$ref" : "#/components/schemas/AlarmEvent"
  }, {
    "$ref" : "#/components/schemas/CloudAlarmEvent"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"SSEventStream": _ss_event_stream_model_schema})

_success_operation_result_value_model_schema = json.loads(
    r"""{
  "title" : "SuccessOperationResult_value",
  "required" : [ "statusCode" ],
  "type" : "object",
  "properties" : {
    "statusCode" : {
      "title" : "statusCode",
      "type" : "integer",
      "description" : "The statusCode of the operation"
    }
  },
  "description" : "The keys will be alarm ids."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update(
    {"SuccessOperationResult_value": _success_operation_result_value_model_schema}
)

_version_response_model_schema = json.loads(
    r"""{
  "required" : [ "name", "version" ],
  "type" : "object",
  "properties" : {
    "version" : {
      "type" : "string",
      "example" : "2.7.0"
    },
    "name" : {
      "type" : "string",
      "example" : "alarm-service"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"VersionResponse": _version_response_model_schema})
