use serde_json::Value;
use url::Url;

#[derive(Debug, PartialEq)]
pub enum SkpError {
    RequiredField,
    UnsupportedVersion,
    InvalidUri,
    InvalidAddress,
    InvalidEntity,
    InvalidTransition,
    InvalidPayload,
    InvalidProvenance,
    InvalidExtensions,
}

pub fn validate_packet(v: &Value) -> Result<(), SkpError> {
    let o = v.as_object().ok_or(SkpError::RequiredField)?;
    for k in ["skp","id","profile","semantic_address","action","subject","reach","provenance","extensions"] {
        if !o.contains_key(k) { return Err(SkpError::RequiredField); }
    }
    if o.get("skp").and_then(Value::as_str) != Some("1.0-draft") {
        return Err(SkpError::UnsupportedVersion);
    }
    for k in ["id","profile"] {
        let s = o.get(k).and_then(Value::as_str).ok_or(SkpError::InvalidUri)?;
        Url::parse(s).map_err(|_| SkpError::InvalidUri)?;
    }
    let a = o.get("semantic_address").and_then(Value::as_object).ok_or(SkpError::InvalidAddress)?;
    if a.get("space").and_then(Value::as_str).unwrap_or("").is_empty() { return Err(SkpError::InvalidAddress); }
    if a.get("coordinates").and_then(Value::as_array).map(|x| x.is_empty()).unwrap_or(true) { return Err(SkpError::InvalidAddress); }
    if !o.get("extensions").map(Value::is_object).unwrap_or(false) { return Err(SkpError::InvalidExtensions); }
    Ok(())
}
