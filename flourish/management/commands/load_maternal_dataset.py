from pprint import pprint
from decimal import Decimal
from dateutil import parser

from django.core.management.base import BaseCommand

from flourish_maternal.models import MaternalDataset


class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Data fine path, csv file')

    def handle(self, *args, **kwargs):
        already_exists = 0
        created = 0
        file_path = kwargs['file_path']
        data = self.data(file_path=file_path)
        
        for data_item in data:
            options = {}
            for field_name in self.all_model_fields:
                options[field_name] = data_item.get(field_name)
            
            # Update identifiers
            options.update(study_child_identifier=data_item.get('bid'))
            options.update(study_maternal_identifier=data_item.get('m_bid'))
            # Convert date to date objects
            try:
                mom_enrolldate = parser.parse(options.get('mom_enrolldate')).date()
            except parser.ParserError:
                options.update(mom_enrolldate=None)
            else:
                options.update(mom_enrolldate=mom_enrolldate)

            try:
                mom_arvstart_date = parser.parse(options.get('mom_arvstart_date')).date()
            except parser.ParserError:
                options.update(mom_arvstart_date=None)
            else:
                options.update(mom_arvstart_date=mom_arvstart_date)
        
            try:
                mom_baseline_hgbdt = parser.parse(options.get('mom_baseline_hgbdt'))
            except parser.ParserError:
                options.update(mom_baseline_hgbdt=None)
            else:
                options.update(mom_baseline_hgbdt=mom_baseline_hgbdt)
            
            try:
                delivdt = parser.parse(options.get('delivdt')).date()
            except parser.ParserError:
                options.update(delivdt=None)
            else:
                options.update(delivdt=delivdt)
            
            try:
                mom_deathdate = parser.parse(options.get('mom_deathdate')).date()
            except parser.ParserError:
                options.update(mom_deathdate=None)
            else:
                options.update(mom_deathdate=mom_deathdate)
            
            try:
                mom_baseline_cd4date = parser.parse(options.get('mom_baseline_cd4date'))
            except parser.ParserError:
                options.update(mom_baseline_cd4date=None)
            else:
                options.update(mom_baseline_cd4date=mom_baseline_cd4date)
            
            try:
                mom_baseline_vldate = parser.parse(options.get('mom_baseline_vldate'))
            except parser.ParserError:
                options.update(mom_baseline_vldate=None)
            else:
                options.update(mom_baseline_vldate=mom_baseline_vldate)
            
            # Convert int values to int objects
            try:
                parity = int(options.get('parity'))
            except ValueError:
                options.update(parity=None)
            else:
                options.update(parity=parity)
            
            try:
                toilet = int(options.get('toilet'))
            except ValueError:
                options.update(toilet=None)
            else:
                options.update(toilet=toilet)
        
            try:
                live_inhouse_number = int(options.get('live_inhouse_number'))
            except ValueError:
                options.update(live_inhouse_number=None)
            else:
                options.update(live_inhouse_number=live_inhouse_number)
            
            try:
                gravida = int(options.get('gravida'))
            except ValueError:
                options.update(gravida=None)
            else:
                options.update(gravida=gravida)
            
            try:
                mom_baseline_cd4 = int(options.get('mom_baseline_cd4'))
            except ValueError:
                options.update(mom_baseline_cd4=None)
            else:
                options.update(mom_baseline_cd4=mom_baseline_cd4)
            
            try:
                mom_baseline_vl = int(options.get('mom_baseline_vl'))
            except ValueError:
                options.update(mom_baseline_vl=None)
            else:
                options.update(mom_baseline_vl=mom_baseline_vl) 
            
            # Convert decimal values to decimal objects
            if options.get('mom_baseline_hgb') and not options.get('mom_baseline_hgb') == '.':
                mom_baseline_hgb = Decimal(options.get('mom_baseline_hgb'))
                options.update(mom_baseline_hgb=mom_baseline_hgb)
            else:
                options.update(mom_baseline_hgb=None)
            try:
                MaternalDataset.objects.get(study_maternal_identifier=data_item.get('m_bid'))
            except MaternalDataset.DoesNotExist:
                MaternalDataset.objects.create(**options)
                created += 1
            else:
                already_exists += 1
        self.stdout.write(self.style.SUCCESS(f'A total of {created} have been creeated'))
        self.stdout.write(self.style.WARNING(f'Total items {already_exists} already existed'))

    def data(self, file_path=None):
        data = []
        f = open(file_path, 'r')
        lines = f.readlines()
        header = lines[0]
        lines.pop(0)
        header = header.strip()
        header = header.split(',')
        self.stdout.write(self.style.WARNING(f'Total items {len(lines)}'))
        for line in lines:
            line = line.strip()
            line = line.split(',')
            data_item = dict(zip(header, line))
            data.append(data_item)
        return data
    
    @property
    def all_model_fields(self):
        """Returns a list of maternal dataset model fields.
        """
        exclude_fields = [
            'created',
            'modified',
            'user_created',
            'user_modified',
            'hostname_created',
            'hostname_modified',
            'revision',
            'device_created',
            'device_modified',
            'id',
            'site',
            'subject_identifier',
            'screening_identifier',
            'study_child_identifier',
            'study_maternal_identifier',]
        fields = []
        for field in MaternalDataset._meta.get_fields():
            if not field.name in exclude_fields:
                fields.append(field.name)
        return fields
            