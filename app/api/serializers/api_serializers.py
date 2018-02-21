from rest_framework import serializers

class ApiSerializers(serializers.ModelSerializer):

    def perform_create(self, serializers):
        import pdb
        pdb.set_trace()
        serializers.save(creator_id = self.request.user.id)
