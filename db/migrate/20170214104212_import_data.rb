class ImportData < ActiveRecord::Migration[5.0]
  def change
    TaxonomyImporter.new.import
  end
end
