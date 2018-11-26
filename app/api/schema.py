import graphene


class Query(graphene.ObjectType):
    name = graphene.String(
        argument=graphene.String(default_value='stranger'))

    def resolve_name(self, info, argument):
        return 'Hello' + argument

schema = graphene.Schema(query=Query)
