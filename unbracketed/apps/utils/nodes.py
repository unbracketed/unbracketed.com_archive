from template_utils.nodes import GenericContentNode

class FlexGenericContentNode( GenericContentNode ):
    """
    Extends the GenericContentNode from template-utils to
    add an option to specify "all" for the content count to retrieve
    all instances of the content type
    """
    def get_content(self, context):
        query_set = self._get_query_set()
        if self.num == 1:
            result = query_set[0]
        elif self.num == 'all':
            result = list(query_set)
        else:
            result = list(query_set[:self.num])
        return { self.varname: result }



