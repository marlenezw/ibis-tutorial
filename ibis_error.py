---------------------------------------------------------------------------
OperationalError                          Traceback (most recent call last)
~/opt/anaconda3/lib/python3.9/site-packages/sqlalchemy/engine/base.py in _execute_context(self, dialect, constructor, statement, parameters, execution_options, *args, **kw)
   1770                 if not evt_handled:
-> 1771                     self.dialect.do_execute(
   1772                         cursor, statement, parameters, context

~/opt/anaconda3/lib/python3.9/site-packages/sqlalchemy/engine/default.py in do_execute(self, cursor, statement, parameters, context)
    716     def do_execute(self, cursor, statement, parameters, context=None):
--> 717         cursor.execute(statement, parameters)
    718 

OperationalError: no such column: t0.SF_Find_Neighborhoods

The above exception was the direct cause of the following exception:

OperationalError                          Traceback (most recent call last)
~/opt/anaconda3/lib/python3.9/site-packages/IPython/core/formatters.py in __call__(self, obj)
    700                 type_pprinters=self.type_printers,
    701                 deferred_pprinters=self.deferred_printers)
--> 702             printer.pretty(obj)
    703             printer.flush()
    704             return stream.getvalue()

~/opt/anaconda3/lib/python3.9/site-packages/IPython/lib/pretty.py in pretty(self, obj)
    392                         if cls is not object \
    393                                 and callable(cls.__dict__.get('__repr__')):
--> 394                             return _repr_pprint(obj, self, cycle)
    395 
    396             return _default_pprint(obj, self, cycle)

~/opt/anaconda3/lib/python3.9/site-packages/IPython/lib/pretty.py in _repr_pprint(obj, p, cycle)
    698     """A pprint that just redirects to the normal repr function."""
    699     # Find newlines and replace them with p.break_()
--> 700     output = repr(obj)
    701     lines = output.splitlines()
    702     with p.group():

~/opt/anaconda3/lib/python3.9/site-packages/ibis/expr/types.py in __repr__(self)
     37 
     38         try:
---> 39             result = self.execute()
     40         except com.TranslationError as e:
     41             output = (

~/opt/anaconda3/lib/python3.9/site-packages/ibis/expr/types.py in execute(self, limit, timecontext, params, **kwargs)
    273           Result of compiling expression and executing in backend
    274         """
--> 275         return self._find_backend().execute(
    276             self, limit=limit, timecontext=timecontext, params=params, **kwargs
    277         )

~/opt/anaconda3/lib/python3.9/site-packages/ibis/backends/base/sql/__init__.py in execute(self, expr, params, limit, **kwargs)
    122         sql = query_ast.compile()
    123         self._log(sql)
--> 124         cursor = self.raw_sql(sql, **kwargs)
    125         schema = self.ast_schema(query_ast, **kwargs)
    126         result = self.fetch_from_cursor(cursor, schema)

~/opt/anaconda3/lib/python3.9/site-packages/ibis/backends/base/sql/alchemy/__init__.py in raw_sql(self, query, results)
    328 
    329     def raw_sql(self, query: str, results=False):
--> 330         return _AutoCloseCursor(super().raw_sql(query))
    331 
    332     def _log(self, sql):

~/opt/anaconda3/lib/python3.9/site-packages/ibis/backends/base/sql/__init__.py in raw_sql(self, query, results)
     84         # is nothing that enforces it. We should find a way to make sure
     85         # `self.con` is always a DBAPI2 connection, or raise an error
---> 86         cursor = self.con.execute(query)  # type: ignore
     87         if cursor:
     88             return cursor

<string> in execute(self, statement, *multiparams, **params)

~/opt/anaconda3/lib/python3.9/site-packages/sqlalchemy/util/deprecations.py in warned(fn, *args, **kwargs)
    388         if not skip_warning:
    389             _warn_with_version(message, version, wtype, stacklevel=3)
--> 390         return fn(*args, **kwargs)
    391 
    392     doc = func.__doc__ is not None and func.__doc__ or ""

~/opt/anaconda3/lib/python3.9/site-packages/sqlalchemy/engine/base.py in execute(self, statement, *multiparams, **params)
   3106         """
   3107         connection = self.connect(close_with_result=True)
-> 3108         return connection.execute(statement, *multiparams, **params)
   3109 
   3110     @util.deprecated_20(

~/opt/anaconda3/lib/python3.9/site-packages/sqlalchemy/engine/base.py in execute(self, statement, *multiparams, **params)
   1261             )
   1262         else:
-> 1263             return meth(self, multiparams, params, _EMPTY_EXECUTION_OPTS)
   1264 
   1265     def _execute_function(self, func, multiparams, params, execution_options):

~/opt/anaconda3/lib/python3.9/site-packages/sqlalchemy/sql/elements.py in _execute_on_connection(self, connection, multiparams, params, execution_options, _force)
    321     ):
    322         if _force or self.supports_execution:
--> 323             return connection._execute_clauseelement(
    324                 self, multiparams, params, execution_options
    325             )

~/opt/anaconda3/lib/python3.9/site-packages/sqlalchemy/engine/base.py in _execute_clauseelement(self, elem, multiparams, params, execution_options)
   1450             linting=self.dialect.compiler_linting | compiler.WARN_LINTING,
   1451         )
-> 1452         ret = self._execute_context(
   1453             dialect,
   1454             dialect.execution_ctx_cls._init_compiled,

~/opt/anaconda3/lib/python3.9/site-packages/sqlalchemy/engine/base.py in _execute_context(self, dialect, constructor, statement, parameters, execution_options, *args, **kw)
   1812 
   1813         except BaseException as e:
-> 1814             self._handle_dbapi_exception(
   1815                 e, statement, parameters, cursor, context
   1816             )

~/opt/anaconda3/lib/python3.9/site-packages/sqlalchemy/engine/base.py in _handle_dbapi_exception(self, e, statement, parameters, cursor, context)
   1993                 util.raise_(newraise, with_traceback=exc_info[2], from_=e)
   1994             elif should_wrap:
-> 1995                 util.raise_(
   1996                     sqlalchemy_exception, with_traceback=exc_info[2], from_=e
   1997                 )

~/opt/anaconda3/lib/python3.9/site-packages/sqlalchemy/util/compat.py in raise_(***failed resolving arguments***)
    205 
    206         try:
--> 207             raise exception
    208         finally:
    209             # credit to

~/opt/anaconda3/lib/python3.9/site-packages/sqlalchemy/engine/base.py in _execute_context(self, dialect, constructor, statement, parameters, execution_options, *args, **kw)
   1769                             break
   1770                 if not evt_handled:
-> 1771                     self.dialect.do_execute(
   1772                         cursor, statement, parameters, context
   1773                     )

~/opt/anaconda3/lib/python3.9/site-packages/sqlalchemy/engine/default.py in do_execute(self, cursor, statement, parameters, context)
    715 
    716     def do_execute(self, cursor, statement, parameters, context=None):
--> 717         cursor.execute(statement, parameters)
    718 
    719     def do_execute_no_params(self, cursor, statement, context=None):

OperationalError: (sqlite3.OperationalError) no such column: t0.SF_Find_Neighborhoods
[SQL: SELECT t0.creation_date, t0.accession_number, t0.artist, t0.credit_line, t0.display_title, t0.display_dimensions, t0.medium, t0.media_support, t0.facility, t0.current_location, t0.location_description, t0.street_address_or_intersection, t0.zip_code, t0.latitude, t0.longitude, t0.number_of_districts, t0.cultural_districts, t0.supervisor_district, t0.the_geom, t0."SF_Find_Neighborhoods", t0."Current_Police_Districts", t0."Current_Supervisor_Districts", t0."Analysis_Neighborhoods", t0."Neighborhoods" 
FROM base."civicArtTable" AS t0 
WHERE t0.artist = ?
 LIMIT ? OFFSET ?]
[parameters: ('Colburn, Adriane', 10000, 0)]
(Background on this error at: https://sqlalche.me/e/14/e3q8)