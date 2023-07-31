#pragma once

#include <mw/exceptions/METIException.h>
#include <mw/util/StringUtil.h>

#define ThrowDatabase(msg) throw DatabaseException(msg, __FUNCTION__)
#define ThrowDatabase_F(msg, ...) throw DatabaseException(StringUtil::Format(msg, __VA_ARGS__), __FUNCTION__)

class DatabaseException : public METIException
{
public:
    DatabaseException(const std::string& message, const std::string& function)
        : METIException("DatabaseException", message, function)
    {

    }
};