import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))
